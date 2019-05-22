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

def loginuser(request):
    username=request.POST.get('username','')
    password = request.POST.get('password', '')
    try:
        user = UserInfo.objects.filter(username=username)
        user1=user[2]
        if user1.password==password:

            return HttpResponseRedirect("/info")

        else:
            return HttpResponse('密码错误')
    except :
        return HttpResponse('用户名不存在')

def regiterUser(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    payname = request.POST.get('payname', '')
    try:
        user = UserInfo.objects.all()  # 获取对于用户名列表
        user1 = []
        for i in user:
            user1.append(i[2])
        if name in user1:
            return HttpResponse('账户名已存在')
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
        return HttpResponse('注册失败')


def putIn(request):
    sname=request.POST.get('sname','')
    age=request.POST.get('age','')
    school=request.POST.get('school','')
    schoolID=request.POST.get('schoolID','')
    studentID=request.POST.get('studentID','')
    email=request.POST.get('email','')
    phone=request.POST.get('phone','')
    stu1=UserInfo()
    stu1.sname=sname
    stu1.age = age
    stu1.school = school
    stu1.schoolID =  schoolID
    stu1.studentID = studentID
    stu1.email = email
    stu1.phone = phone
    stu1.save()
    return HttpResponse('报名成功')

