from django.shortcuts import redirect, render
from taskbook.models import *
from django.contrib.auth import authenticate,login,logout



def login(request):
    if request.method=='POST':
        #stores the username given in frontend to nusername variable
        nusername=request.POST['username']  
        npassword=request.POST['password']
        user=authenticate(request,username=nusername,password=npassword)
        if user is not None:
            login(request,user)
            return redirect('homepage')
    return render('request','taskbook/login.html')


# django logout function flushes out the users session and logout the active user
def logout(request):
    logout(request)
    return redirect('homepage')
    

#create users or handle signup
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







#alternative method to login authentication
# def login(request):
#     if request.method=='POST':
#         #stores the username given in frontend to nusername variable
#         nusername=request.POST['username']  
#         npassword=request.POST['password']
#         try:
#             #select the user object containing the given username and password
#             user = UserInfo.objects.get(username=nusername , password=npassword) 
#             return render(request,'taskbook/home.html',{'user':user})
#         except UserInfo.DoesNotExist:
#             error_message='Invalid credintial'
#             return render(request,'taskbook/login.html',{'error_message':error_message})
#     return render(request, 'taskbook/login.html')