from django.contrib import admin
from django.urls import path, include

## this is for development image hosting
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('exif/<str:filename>', views.imageView),
    path('media/<str:filename>',views.document_view),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', views.signout, name='logout'),
    path('register', views.register, name='register'),
    path('admin', views.admin, name='admin'),
    path('profile', views.profile, name='profile'),
    path('bot/exif/<str:userid>/<str:filename>', views.vic_imageView),
    path('bot/media/<str:userid>/<str:filename>',views.vic_document_view),
]
