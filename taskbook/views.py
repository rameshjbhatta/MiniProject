from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'taskbook/login.html')

def signup(request):
    return render(request,'taskbook/signup.html')

def create(request):
    return render(request,'taskbook/create.html')

def home(request):
    return render(request,'taskbook/home.html')