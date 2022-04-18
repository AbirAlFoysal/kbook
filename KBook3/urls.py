from django.contrib import admin
from django.urls import path, include
from booksite.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('',home.as_view(), name="home" ),
    
    

]
