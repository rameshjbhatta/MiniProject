from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
        name=models.CharField(max_length=250,null=False,blank=False)
        username=models.CharField(max_length=250,unique=True, null=False,blank=False)
        email=models.EmailField(max_length=250,null=False,blank=False)
        mobile=models.IntegerField(null=True,blank=True)
        password=models.CharField(max_length=100,null=False,blank=False)

        def __str__(self):
                return self.name
    
        class Meta:
                db_table = "userinfo"

class TaskInfo(models.Model): 
    
      usertask = models.CharField(blank=False,null=False,max_length=150)
      taskname=models.CharField(max_length=250)  
      location=models.CharField(max_length=250) 
      mobile=models.IntegerField()
      timedate=models.DateTimeField() 
      details=models.TextField(max_length=400) 

      def __str__(self):
                return self.taskname
    
      class Meta:
        db_table = "taskinfo"
