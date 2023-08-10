from django.db import models

# Create your models here.
class UserInfo(models.Model):
        name=models.CharField(max_length=250,null=False,blank=False)
        username=models.CharField(max_length=250,null=False,blank=False)
        email=models.EmailField(max_length=250,null=False,blank=False)
        mobile=models.IntegerField(null=True,blank=True)
        password=models.CharField(max_length=100,null=False,blank=False)

class TaskInfo(models.Model): 
      taskname=models.CharField(max_length=250)  
      location=models.CharField(max_length=250) 
      mobile=models.IntegerField()
      timedate=models.DateTimeField() 
      details=models.TextField(max_length=400) 
