from django.shortcuts import render

from django.http import HttpResponseRedirect
from .models import UserInfo,ItemsInfo
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'login/index.html')
def loginHTML(request):
    return render(request,'PGTP/login.html')

def infoHTML(request):
    return render(request,'PGTP/putin.html')

def regiterHTML(request):
    return render(request,'login/regiter.html')

def addItemHTML(request):
    return render(request,'login/addItem.html')

def showHTML(request):
    return render(request, 'login/show.html')

def loginuser(request):
    username=request.POST.get('username','')
    password = request.POST.get('password', '')
    try:
        ItemList = ItemsInfo.objects.all()
        myuser = UserInfo.objects.get(account=username)
        # user1=user[2]
        if myuser.password==password:

            return render(request,"login/show.html",{"items":ItemList})

        else:
            return HttpResponse('密码错误')
    except Exception as e:
        print(e)
        return HttpResponse(e)

def regiterUser(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    payname = request.POST.get('payname', '')
    try:
        user = UserInfo.objects.filter(account=username)
        if 0:
            print(1)
            # user1 = user[2]
            # if name == user1:
            #     return HttpResponse('账户名已存在')
        else:
            user1=UserInfo()
            user1.password = password
            user1.account = username
            user1.username = name
            user1.email =email
            user1.payAccount = payname
            user1.save()
            return HttpResponse('注册成功')
    except Exception as e:
        print(e)
        return HttpResponse(e)

def gitUp(request):
    itmname = request.POST.get('itmname', '')
    cost = request.POST.get('cost', '')
    describe = request.POST.get('describe', '')
    if itmname == None or cost ==None:
        return HttpResponse('请填写完整信息')
    else:
        item= ItemsInfo()
        item.iCost =cost
        item.iDescribe = describe
        item.iName = itmname
        item.save()
        return HttpResponse('物品上传成功')

