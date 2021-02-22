from django.http import JsonResponse
from django.shortcuts import render

from shop.admin import returnMsg
from shop.models import employee, shop


class Employee:
    def __init__(self):
        super().__init__()
        self.POST = None

    def employee(self):
        return render(self, 'employee.html')

    def addEmployee(self):
        try:
            name = self.POST.get('name')
            age = self.POST.get('age')
            sex = self.POST.get('sex')
            createTime = self.POST.get('createTime')
            salary = self.POST.get('salary')
            shopId = self.POST.get('shopId')
            emp = employee.objects.create(
                name=name,
                age=age,
                sex=sex,
                createTime=createTime,
                salary=salary,
                shopId=shopId
            )
            emp.save()
            return JsonResponse(returnMsg.Success(msg='添加店员成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def showEmployee(self):
        try:
            allEmployee = employee.objects.all()
            page = int(self.POST.get('page'))
            limit = int(self.POST.get('limit'))
            total = len(allEmployee)
            showEmployees = allEmployee[limit * (page - 1):limit * page]
            data = list()
            for emp in showEmployees:
                content = dict()
                content['id'] = emp.id
                content['name'] = emp.name
                content['age'] = emp.age
                content['sex'] = emp.sex
                content['createTime'] = emp.createTime.strftime('%Y-%m-%d')
                content['salary'] = emp.salary
                content['shop'] = shop.objects.get(id=emp.shopId).name
                data.append(content)
            return JsonResponse(returnMsg.Success(data=data, total=total), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def updateEmployee(self):
        try:
            empId = self.POST.get('id')
            name = self.POST.get('name')
            age = self.POST.get('age')
            sex = self.POST.get('sex')
            createTime = self.POST.get('createTime')
            salary = self.POST.get('salary')
            shopId = self.POST.get('shopId')
            employee.objects.filter(id=empId).update(
                name=name,
                age=age,
                sex=sex,
                createTime=createTime,
                salary=salary,
                shopId=shopId
            )
            return JsonResponse(returnMsg.Success(msg='修改成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def delEmployee(self):
        try:
            empId = self.POST.get('id')
            employee.objects.filter(id=empId).delete()
            return JsonResponse(returnMsg.Success(msg='删除成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    def aEmployee(self):
        return render(self, 'addemployee.html')
