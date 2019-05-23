from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    payAccount = models.CharField(max_length=60)
    def __str__(self):
        return self.username



class ItemsInfo(models.Model):
    iName = models.CharField(max_length=40)
    iCost = models.CharField(max_length=20)
    iDescribe = models.CharField(max_length=200)