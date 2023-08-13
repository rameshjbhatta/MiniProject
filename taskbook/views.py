from django.shortcuts import redirect, render
from taskbook.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    tasks = TaskInfo.objects.all()  # extract all tasks from the TasInfo table and rendered to the home
    return render(request, 'taskbook/home.html', {'tasks': tasks})



def loginHandler(request):
    if request.method=='POST':
        #stores the username given in frontend to nusername variable
        nusername=request.POST['username']  
        npassword=request.POST['password']
        try:
            #select the user object containing the given username and password
            user = UserInfo.objects.get(username=nusername , password=npassword)
            tasks=TaskInfo.objects.all() 
            return render(request,'taskbook/home.html',{'user':user,'tasks':tasks})
        except UserInfo.DoesNotExist:
            error_message='Invalid credintial'
            return render(request,'taskbook/login.html',{'error_message':error_message})
    return render(request, 'taskbook/login.html')



# django logout function flushes out the users session and logout the active user
def logoutHandler(request):
    logout(request)
    return redirect('loginpage')


#create users or handle signup
def signupHandler(request):
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
    

     
def createTask(request):
    if request.method=='POST':
        taskid =request.POST['taskid']
        tname=request.POST['taskname']
        tlocation=request.POST['location']
        tmobile=request.POST['mobile']
        ttimedate=request.POST['timedate']
        tdetails=request.POST['details']
        tasks=TaskInfo(usertask=taskid,taskname=tname,location=tlocation,mobile=tmobile,timedate=ttimedate,details=tdetails)
        try:
            tasks.save()  # This will save the object to the database
            success_message="Task Created Successfully!"
            return render(request,'taskbook/create.html',{'tasks':tasks,'messages':success_message} )
        except Exception as e:
            error_message="Sorry, Task Not Created:"
            return render(request,'taskbook/create.html',{'messages':error_message} )  
    tasks = TaskInfo.objects.all()
    return render(request,'taskbook/create.html',{'tasks':tasks} )


def updateTask(request,id):
    tasks=TaskInfo.objects.get(id=id)#gets the tasks that you had clicked to update
    if request.method=='POST':
        tasks.usertask =request.POST['taskid'] #posta the updated data to that field
        tasks.taskname=request.POST['taskname']
        tasks.location=request.POST['location']
        tasks.mobile=request.POST['mobile']
        tasks.timedate=request.POST['timedate']
        tasks.details=request.POST['details']
        tasks.save()
        return redirect('homepage')
    return render(request,'taskbook/update.html',{'tasks':tasks})# these tasks are the older information of task 



def deleteTask(id):
    tasks=TaskInfo.objects.get(id=id)
    tasks.delete()
    return redirect('homepage')


def searchTask(request):
    query = request.GET.get('q')  # Get the data from the GET request you want to search
    tasks=None
    if query:
       tasks = TaskInfo.objects.filter(Q(usertask__icontains=query)|Q(location__icontains=query)|Q(mobile__icontains=query)|Q(taskname__icontains=query)|Q(details__icontains=query)|Q(timedate__icontains=query)) # for complex search import Q from db.models
       if tasks:
            return render(request, 'taskbook/search.html', {
                'tasks': tasks,
                'query': query,
            })
       else:
            message = 'No matching tasks found.'
            return render(request, 'taskbook/search.html', {'message': message})
    else:
        message = 'Please enter a search query.'
        return render(request, 'taskbook/search.html', {'message': message})









# # method to login authentication for the djangouser model
# def loginHandler(request):
#     if request.method=='POST':
#         username=request.POST.get('username') 
#         password=request.POST.get('password')
#         print(username,password)
#         user=authenticate(username=username,password=password)
#         print(user)
#         if user is not None:
#             login(request,user)
#             return redirect('homepage')  
#         else:
#             print("invalid credintials") 
#     return render(request,'taskbook/login.html')

