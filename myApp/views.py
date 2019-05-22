from django.shortcuts import render
# Create your views here. 在view里边定义视图
from django.http import HttpResponse
from .models import Grades,Students
#在Django中，视图是对web请求进行回应
def index(request):
    return HttpResponse('sunck is a good man!')
def detail(request):
    return HttpResponse('这里是2222222')

def grades(request):#在视图里 去模板里取数据 传递数据给模板
    # 拿出所有班级对象列表
    gradesList = Grades.objects.all()
    # 将数据传递给模板 ，模板渲染页面 ，再将渲染好的页面返回给浏览器
    return render(request,'myApp/grades.html',{'grades':gradesList})
def students(request):#在视图里 去模板里取数据 传递数据给模板
    # 拿出所有学生对象列表
    studentsList = Students.objects.all()
    # 将数据传递给模板 ，模板渲染页面 ，再将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{'students':studentsList})

def gradesStudents(request,num):
    grade = Grades.objects.get(pk = num )#找到这个班级
    studentsList = grade.students_set.all#获取这个班级所有的学生对象
    return render(request, 'myApp/students.html', {'students': studentsList})