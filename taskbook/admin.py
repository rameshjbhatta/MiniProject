from django.contrib import admin
from taskbook.models import *

# Register your models here.
class TaskAdminView(admin.ModelAdmin):
    list_display=['id','usertask','taskname','location','mobile','timedate','details']
   

class UserInfoAdminView(admin.ModelAdmin):
    list_display=['id','name','username','email','mobile','password']  


admin.site.register(TaskInfo,TaskAdminView)
admin.site.register(UserInfo,UserInfoAdminView)
