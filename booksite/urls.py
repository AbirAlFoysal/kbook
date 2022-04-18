# from django.urls import path,include
from django.contrib import admin
from django.urls import  path, include

from .views import UserPostListView

urlpatterns = [
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]