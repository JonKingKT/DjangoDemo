from django.contrib import admin
from .models import Grades,Students#引入两张表
# Register your models here.  在这里注册你的模型 站点管理 作为管理员来操作数据

class StudentsInfo(admin.TabularInline):#创建班级时加两个学生
    model = Students
    extra = 2


class GrandesAdmin(admin.ModelAdmin):#自定义管理页面
    # 列表页属性
    inlines = [StudentsInfo]#增加行 注册时班级同时加入学生
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']  # 显示字段设置
    list_filter = ['gname']  # 过滤字段设置
    search_fields = ['gname']  # 搜索字段设置
    # list_per_page = 5  # 分页设置  每5条是一页
    # # 添加，修改页属性
    # fields = []  # 规定属性的先后顺序
    fieldsets = [("num",{"fields":['ggirlnum', 'gboynum']}),
                     ("base", {"fields":["gname", "gdate", "isDelete"]}),]  # 给属性分组 注意：fields与fieldsets不能同时使用


@admin.register(Students)#使用装饰器进行注册
class StudentsAdmin(admin.ModelAdmin):#自定义管理页面

    def gender(self):#布尔值显示问题 自己定义函数
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'#这个函数的描述 用于设置页面列的名称

    list_display = ['pk', 'sname', gender,'sage','scontend','sgrade','isDelete']  # 显示字段
    list_per_page = 10




#注册 另一种方式  使用装饰器进行注册 23行
admin.site.register(Grades,GrandesAdmin)
# admin.site.register(Students,StudentsAdmin)
