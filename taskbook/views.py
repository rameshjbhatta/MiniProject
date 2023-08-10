from django.shortcuts import redirect, render
from taskbook.models import *

# Create your views here.
def index(request):
    return render(request, 'taskbook/login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        UserInfo.objects.create(name=name,username=username,email=email,mobile=mobile,password=password)
        return render(request,'taskbook/login.html')
    else:    
       return render(request,'taskbook/signup.html')

def create(request):
    return render(request,'taskbook/create.html')

def home(request):
    return render(request,'taskbook/home.html')