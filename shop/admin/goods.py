from django.http import JsonResponse

from shop.admin import returnMsg
from shop.models import goods, shop


class Goods:
    def __init__(self):
        super().__init__()
        self.POST = None

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
                goodsType=goodsType,
                goodsSum=goodsSum,
                price=price,
                per=per,
                shopId=shopId
            )
            go.save()
            return JsonResponse(returnMsg.Success(msg='添加成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def showGoods(self):
        try:
            allGoods = goods.objects.all()
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
                content['shopId'] = shop.objects.get(id=go.shopId).name
                data.append(content)
            return JsonResponse(returnMsg.Success(data=data, total=total), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Success(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def updateGoods(self):
        try:
            goodsId = self.POST.get('id')
            name = self.POST.get('name')
            goodsType = self.POST.get('type')
            goodsSum = self.POST.get('sum')
            price = self.POST.get('price')
            per = self.POST.get('per')
            shopId = self.POST.get('shopId')
            goods.objects.filter(id=goodsId).update(
                name=name,
                goodsType=goodsType,
                goodsSum=goodsSum,
                price=price,
                per=per,
                shopId=shopId
            )
            return JsonResponse(returnMsg.Success(msg='修改成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def delGoods(self):
        try:
            goodsId = self.POST.get('id')
            goods.objects.filter(id=goodsId).delete()
            return JsonResponse(returnMsg.Success(msg='删除成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))
