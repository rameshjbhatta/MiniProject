from django.contrib import admin
from taskbook.models import *

# Register your models here.
class TaskAdminView(admin.ModelAdmin):
    fields=['id','taskname','location','mobile','timedate','details']
   

class UserAdminView(admin.ModelAdmin):
    fields=['id','name','username','email','mobile','password']    

admin.site.register(TaskInfo,TaskAdminView)
admin.site.register(UserInfo,UserAdminView)