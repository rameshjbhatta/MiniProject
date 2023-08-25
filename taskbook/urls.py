
from taskbook import views
from django.urls import path
from taskbook.views import *

appname='taskbook'
urlpatterns = [
    path('',views.loginHandler, name='loginpage'),
    path('logout/',views.logoutHandler, name='logoutpage'),
    path('home/',views.home, name='homepage'),
    path('signup/',views.signupHandler, name='signuppage'),
    path('create/',views.createTask, name='createpage'),
    path('update/<int:id>',views.updateTask, name='updatepage'),
    path('delete/<int:id>',views.deleteTask, name='deletepage'),
    path('search/', views.searchTask,name="searchpage"),
]