from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from shop.admin import returnMsg


# Create your views here.
class Login:
    def __init__(self):
        self.POST = None

    def login(self):
        return render(self, 'login.html')

    def uLogin(self):
        if self.POST:
            username = self.POST.get('username')
            password = self.POST.get('password')
            # 进行登录认证,
            user = authenticate(username=username, password=password)
            # 判断用户是否存在
            if user is not None:
                if user.is_superuser:
                    # 这里的登录, 表示的是将用户信息添加到session中
                    login(self, user)
                    return JsonResponse(returnMsg.Success(msg='登录成功'))
                else:
                    return JsonResponse(returnMsg.Error(msg='抱歉您没有这个权限'))
            else:
                return JsonResponse(returnMsg.Error(msg='用户名或密码错误'))
        else:
            return render(self, 'login.html')
