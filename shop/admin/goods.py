from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from shop.admin import returnMsg
from shop.admin.returnMsg import change
from shop.models import goods, shop


class Goods:
    def __init__(self):
        super().__init__()
        self.user = None
        self.POST = None

    @login_required
    def goods(self):
        user = User.objects.get(id=self.user.id)
        context = dict()
        context['date'] = user
        return render(self, 'goods.html', context)

    @login_required
    def aGoods(self):
        user = User.objects.get(id=self.user.id)
        context = dict()
        context['date'] = user
        print(user)
        return render(self, 'addgoods.html', context)

    @login_required
    def addGoods(self):
        try:
            name = self.POST.get('name')
            goodsType = self.POST.get('type')
            goodsSum = self.POST.get('sum')
            price = self.POST.get('price')
            per = self.POST.get('per')
            shopId = self.POST.get('shopId')
            go = goods.objects.create(
                name=name,
                type=goodsType,
                sum=goodsSum,
                price=price,
                per=per,
                shopId=shopId
            )
            go.save()
            return JsonResponse(returnMsg.Success(msg='添加成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    @login_required
    def showGoods(self):
        try:
            name = change(self.POST.get('name'))
            goodsType = change(self.POST.get('type'))
            shopId = self.POST.get('shop')
            if shopId == '':
                allGoods = goods.objects.filter(name__contains=name, type__contains=goodsType)
            else:
                allGoods = goods.objects.filter(name__contains=name, type__contains=goodsType, shopId=shopId)
            total = len(allGoods)
            page = int(self.POST.get('page'))
            limit = int(self.POST.get('limit'))
            showGoods = allGoods[limit * (page - 1):limit * page]
            data = list()
            for go in showGoods:
                content = dict()
                content['id'] = go.id
                content['name'] = go.name
                content['type'] = go.type
                content['sum'] = go.sum
                content['price'] = go.price
                content['per'] = go.price
                content['shopId'] = go.shopId
                content['shopname'] = shop.objects.get(id=go.shopId).name
                data.append(content)
            return JsonResponse(returnMsg.Success(data=data, total=total), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Success(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    @login_required
    def updateGoods(self):
        try:
            goodsId = self.POST.get('id')
            name = self.POST.get('name')
            goodsType = self.POST.get('type')
            goodsSum = self.POST.get('sum')
            price = self.POST.get('price')
            per = self.POST.get('per')
            shopId = self.POST.get('shopId')
            # print(goodsId, name, goodsType, goodsSum, price, per, shopId)
            goods.objects.filter(id=goodsId).update(
                name=name,
                type=goodsType,
                sum=goodsSum,
                price=price,
                per=per,
                shopId=shopId
            )
            return JsonResponse(returnMsg.Success(msg='修改成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    @login_required
    def delGoods(self):
        try:
            goodsId = self.POST.get('id')
            goods.objects.filter(id=goodsId).delete()
            return JsonResponse(returnMsg.Success(msg='删除成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))
