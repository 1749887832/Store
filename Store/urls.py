"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from shop.admin import index
from shop.admin import store
from shop.admin import employee
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login.login),
    path('userLogin/', views.Login.uLogin),
    path('index/', index.Index.toIndex),
    path('store/', store.Store.store),
    path('addstore/',store.Store.addStore),
    path('aStore/',store.Store.aStore),
    path('showstore/',store.Store.showStore),
    path('delstore/',store.Store.delStore),
    path('updatestore/',store.Store.updateStore),
    path('employee/',employee.Employee.employee),
    path('showemployee/',employee.Employee.showEmployee),
    path('addemployee/',employee.Employee.aEmployee),
    path('showallstore/',store.Store.showAllStore),
    path('aEmployee/',employee.Employee.addEmployee),
]
