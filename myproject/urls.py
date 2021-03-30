"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from myapp import views
from accounts import views2
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.mainpage,name="home"),
    path('features',views.featurespage,name="features"),
    path('index',views.index,name="index"),
    path('book',views.book,name="book"),
    path('edit',views.edit,name="edit"),
    path('dashboard',views2.dashboard,name="dashboard"),
    path('register',views2.register,name="register"),
    path('login',views2.login,name="login"),
    path('logout',views2.logout,name="logout")
]
