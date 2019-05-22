from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    payAccount = models.CharField(max_length=60)
    def __str__(self):#操作时可以直接看到班级名字
        return self.username



# class UserInfo(models.Model):
#     sname = models.CharField(max_length=8)
#     age = models.IntegerField()
#     school = models.CharField(max_length=20)
#     schoolID = models.CharField(max_length=20)
#     studentID = models.CharField(max_length=18)
#     email = models.CharField(max_length=20)
#     phone = models.CharField(max_length=20)
#     def __str__(self):
#         return self.sname

class ItemsInfo(models.Model):
    iName = models.CharField(max_length=40)
    iCost = models.CharField(max_length=20)
    iDescribe = models.CharField(max_length=200)