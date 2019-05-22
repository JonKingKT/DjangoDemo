from django.urls import path,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views
#通过path的方式匹配
urlpatterns = [
    path('', views.index),
    path('login', views.loginHTML),
    path('loginuser', views.loginuser , name='loginuser'),
    path('regiterUser',views.regiterUser,name='regiterUser'),
    path('info', views.infoHTML),
    path('putIn',views.putIn,name='putIn'),
    path('regiter',views.regiterHTML)

]

urlpatterns += staticfiles_urlpatterns()