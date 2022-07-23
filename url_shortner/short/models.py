from django.db import models
from datetime import datetime
from django.utils import timezone
#in case database is not creating after droping table drop database and create in again then try it will work
class myurls(models.Model):
    url = models.CharField(max_length = 1000)
    username=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    uid=models.CharField(max_length=200,primary_key=True,default="jj")
    def __str__(self):
        return self.url
class imp_urls(models.Model):
    uid = models.CharField(max_length = 200,default="")
    target = models.CharField(max_length = 1000)
    username=models.CharField(max_length=1000,default="null")
    def __str__(self):
        return self.url
class user_feedback(models.Model):
    username=models.CharField(max_length=1000)
    comments=models.CharField(max_length=5000)
    date=models.DateTimeField(default=timezone.now)