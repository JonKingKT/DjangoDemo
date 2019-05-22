from django.urls import path,re_path
from django.conf.urls import url
from . import views
#通过path的方式匹配
urlpatterns = [
    path('', views.index),
    path('2/', views.detail),
    path('grades/',views.grades),
    path('students/',views.students),
    re_path('grades/(\d+)',views.gradesStudents)#路径中包含正则表达式时 使用re_path

]