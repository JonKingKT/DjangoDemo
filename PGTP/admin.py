from django.contrib import admin
from .models import UserInfo,ItemsInfo#引入两张表
# Register your models here.
@admin.register(UserInfo)#使用装饰器进行注册
class StudentsAdmin(admin.ModelAdmin):#自定义管理页面
    list_display = ['username', 'password', 'account', 'email', 'payAccount']  # 显示字段
    list_per_page = 10



@admin.register(ItemsInfo)#使用装饰器进行注册
class useraccountAdmin(admin.ModelAdmin):#自定义管理页面
    list_display = ['iName', 'iCost','iDescribe']  # 显示字段