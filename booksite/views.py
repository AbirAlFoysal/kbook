import imp
from django.shortcuts import redirect, render, get_object_or_404,render
from requests import post
from .models import book
from django.contrib.auth.models import User
from django.views.generic import ListView
# Create your views here.

# Create your views here.
class home(ListView):
    model = book
    template_name = 'home.html'
    context_object_name = 'books'

