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
from django.urls import path
from taskbook import views
from django.conf.urls.static import static


admin.site.site_header='Task Book'
admin.site.index_title='TaskBook Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginHandler, name='loginpage'),
    path('logout/',views.logoutHandler, name='logoutpage'),
    path('home/',views.home, name='homepage'),
    path('signup/',views.signupHandler, name='signuppage'),
    path('create/',views.createTask, name='createpage'),
    path('update/<int:id>',views.updateTask, name='updatepage'),
    path('delete/<int:id>',views.deleteTask, name='deletepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
