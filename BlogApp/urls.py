"""
URL configuration for BlogApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import Registration_View
from app.views import Blog_View
from app.views import Create_Blog_View
from app.views import Login_View
from app.views import Home_View
from app.views import Logout_View
from app.views import Single_Blog_View
from app.views import Delete_blog_View
from app.views import Update_Diary_View





urlpatterns = [
    path('', Home_View.as_view(),name='home'),       #  for home page

    path('reg/', Registration_View.as_view(),name='reg'),               #  for registration page

    path('all_blog/', Blog_View.as_view(),name='all_blog'),          #  for seeing all blogs

    path('blog/', Create_Blog_View.as_view(),name='blog'),               #  for creating a new blog

    path('log/', Login_View.as_view(),name='log'),                       #  for login

    path('logout/', Logout_View.as_view(),name='logout'),                    #  for logout

    path('single_blog/<int:pk>', Single_Blog_View.as_view(),name='single_blog'),                 #  for view a single blog
    
    path('delete_blog/<int:pk>', Delete_blog_View.as_view(),name='delete_blog'),                     #  for delete a blog

    path('update_blog/<int:pk>', Update_Diary_View.as_view(),name='update_blog'),                #  for update a blog


]
