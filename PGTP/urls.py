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
    path('regiter',views.regiterHTML),
    path('addItem',views.addItemHTML),
    path('gitUp',views.gitUp,name='gitUp'),
    path('show',views.showHTML)

]

urlpatterns += staticfiles_urlpatterns()