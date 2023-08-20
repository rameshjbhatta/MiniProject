"""
URL configuration for MiniProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.db import router
from django.urls import include, path
from taskbook import views
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskbook.views import *

router = DefaultRouter()
router.register(r'userinfos', UserInfoviewsets)
# router.register(r'taskinfos', TaskInfoviewsets)


admin.site.site_header='Task Book'
admin.site.index_title='TaskBook Administration'


urlpatterns = [
    path('', include(router.urls)),
    path('taskapi/',TaskInfoList.as_view(),name='tasklist'),
    path('admin/', admin.site.urls),
    path('login/',views.loginHandler, name='loginpage'),
    path('logout/',views.logoutHandler, name='logoutpage'),
    path('home/',views.home, name='homepage'),
    path('signup/',views.signupHandler, name='signuppage'),
    path('create/',views.createTask, name='createpage'),
    path('update/<int:id>',views.updateTask, name='updatepage'),
    path('delete/<int:id>',views.deleteTask, name='deletepage'),
    path('search/', views.searchTask,name="searchpage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
