import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from shop.admin import returnMsg
from shop.admin.returnMsg import change
from shop.models import employee, shop


class Employee:
    def __init__(self):
        super().__init__()
        self.user = None
        self.POST = None

    @login_required
    def employee(self):
        user = User.objects.get(id=self.user.id)
        context = dict()
        context['date'] = user
        return render(self, 'employee.html', context)

    @login_required
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

    @login_required
    def showEmployee(self):
        try:
            page = int(self.POST.get('page'))
            limit = int(self.POST.get('limit'))
            salary_min = 0 if self.POST.get('salary_min') == '' else self.POST.get('salary_min')
            salary_max = 9999999999999 if self.POST.get('salary_max') == '' else self.POST.get('salary_max')
            age_min = 0 if self.POST.get('age_min') == '' else self.POST.get('age_min')
            age_max = 9999999999999 if self.POST.get('age_max') == '' else self.POST.get('age_max')
            shopId = self.POST.get('shopId')
            createTime = self.POST.get('createTime')
            if createTime == '':
                createTime = '0001-1-1 至 9999-12-31'
            times = createTime.split('至')
            start_time = datetime.datetime(year=int(times[0].split('-')[0]), month=int(times[0].split('-')[1]),
                                           day=int(times[0].split('-')[2]), hour=0, minute=0, second=0)
            end_time = datetime.datetime(year=int(times[1].split('-')[0]), month=int(times[1].split('-')[1]),
                                         day=int(times[1].split('-')[2]), hour=0, minute=0, second=0)
            sex = change(self.POST.get('sex'))
            name = change(self.POST.get('name'))
            # print(name, sex, age_min, age_max, salary_min, salary_max, shopId, createTime)
            if shopId == '':
                allEmployee = employee.objects.filter(name__contains=name, sex__contains=sex, salary__range=[salary_min, salary_max], age__range=[age_min, age_max], createTime__range=[start_time, end_time])
            else:
                allEmployee = employee.objects.filter(name__contains=name, sex__contains=sex, salary__range=[salary_min, salary_max], age__range=[age_min, age_max], createTime__range=[start_time, end_time],
                                                      shopId=shopId)
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
                content['shopId'] = emp.shopId
                content['shop'] = shop.objects.get(id=emp.shopId).name
                data.append(content)
            return JsonResponse(returnMsg.Success(data=data, total=total), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    @login_required
    def updateEmployee(self):
        try:
            empId = self.POST.get('id')
            name = self.POST.get('name')
            age = self.POST.get('age')
            sex = self.POST.get('sex')
            createTime = self.POST.get('updateTime')
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

    @login_required
    def delEmployee(self):
        try:
            empId = self.POST.get('id')
            employee.objects.filter(id=empId).delete()
            return JsonResponse(returnMsg.Success(msg='删除成功'), safe=False, json_dumps_params=({'ensure_ascii': False}))
        except Exception as e:
            return JsonResponse(returnMsg.Error(msg=str(e)), safe=False, json_dumps_params=({'ensure_ascii': False}))

    @login_required
    def aEmployee(self):
        user = User.objects.get(id=self.user.id)
        context = dict()
        context['date'] = user
        return render(self, 'addemployee.html', context)
