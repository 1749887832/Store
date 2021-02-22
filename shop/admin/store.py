from django.http import JsonResponse
from django.shortcuts import render

from shop.admin import returnMsg
from shop.admin.returnMsg import change
from shop.models import shop


class Store:
    def __init__(self):
        super().__init__()
        self.POST = None

    def store(self):
        return render(self, 'stroe.html')

    def showStore(self):
        try:
            page = int(self.POST.get('page'))
            limit = int(self.POST.get('limit'))
            name = change(self.POST.get('name'))
            price_min = 0 if self.POST.get('price_min') == '' else self.POST.get('price_min')
            price_max = 99999999999 if self.POST.get('price_max') == '' else self.POST.get('price_max')
            storeType = change(self.POST.get('type'))
            boss = change(self.POST.get('boss'))
            shopData = shop.objects.filter(name__contains=name, type__contains=storeType, boss__contains=boss, area__range=[price_min, price_max])
            total = len(shopData)
            showData = shopData[limit * (page - 1):limit * page]
            data = list()
            for i in showData:
                content = dict()
                content['id'] = i.id
                content['name'] = i.name
                content['area'] = i.area
                content['boss'] = i.boss
                content['type'] = i.type
                data.append(content)
            return JsonResponse(returnMsg.Success(data=data, total=total))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)))

    def addStore(self):
        return render(self, 'addstore.html')

    def aStore(self):
        try:
            name = self.POST.get('name')
            area = self.POST.get('area')
            boss = self.POST.get('boss')
            storeType = self.POST.get('type')
            shopStore = shop.objects.create(
                name=name,
                area=area,
                boss=boss,
                type=storeType
            )
            shopStore.save()
            return JsonResponse(returnMsg.Success(msg='添加成功'), safe=False, json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            print(e)
            return JsonResponse(returnMsg.Error())

    def delStore(self):
        try:
            shopId = self.POST.get('id')
            print(shopId)
            return JsonResponse(returnMsg.Success(msg='删除成功'), safe=False, json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params={'ensure_ascii': False})

    def updateStore(self):
        print(self)

        try:
            shopId = self.POST.get('id')
            name = self.POST.get('name')
            area = self.POST.get('area')
            boss = self.POST.get('boss')
            storeType = self.POST.get('type')
            print(shopId, name, area, boss, storeType)
            shop.objects.filter(id=shopId).update(
                name=name,
                area=area,
                boss=boss,
                type=storeType
            )
            return JsonResponse(returnMsg.Success(msg='修改成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params={'ensure_ascii': False})

    def showAllStore(self):
        try:
            allStore = shop.objects.all()
            data = list()
            for store in allStore:
                content = dict()
                content['id'] = store.id
                content['name'] = store.name
                data.append(content)
            return JsonResponse(returnMsg.Success(data=data), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params={'ensure_ascii': False})
