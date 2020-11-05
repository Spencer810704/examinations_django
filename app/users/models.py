from django.db import models
from django.db.models import CASCADE


# 用戶表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    job_title = models.CharField(max_length=25)


# 用戶詳細訊息
class User_Info(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='communicate_information', on_delete=CASCADE)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15)
