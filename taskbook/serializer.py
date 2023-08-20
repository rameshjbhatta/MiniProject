from rest_framework import serializers
from .models import *


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields=['id','name','username','email','mobile','password']


class TaskInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskInfo
        fields="__all__"