from django.db import models
# Create your models here.
#这里存放数据库模型
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()#班级女生数量
    gboynum = models.IntegerField()#班级男生数量
    isDelete = models.BooleanField(default=False)#是否删除 默认否
    def __str__(self):#操作时可以直接看到班级名字
        return self.gname

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)#先默认为男生
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)#关联外键 多个学生对应一个班级
#主键会在生成时自动添加，并且值为自动增加
    def __str__(self):
        return self.sname
