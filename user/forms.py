from pickle import FALSE
from typing_extensions import Required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sqlalchemy import false
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    department = forms.CharField(max_length=6, required = True)
    batch = forms.CharField(max_length=4, required = True)
    hometown = forms.CharField(max_length=250, required = False)

    class Meta:
        model = User
        fields = ['username', 'department','batch','hometown', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    batch = forms.CharField(max_length=4)

    class Meta:
        model = User
        fields = ['username', 'batch']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(max_length=1500, required = False)
    phone = forms.IntegerField(required = False)
    website = forms.URLField(required = False)
    facebook = forms.URLField(required = False)
    instagram = forms.URLField(required = False)
    college = forms.CharField(max_length=250, required = False)
    school = forms.CharField(max_length=250, required = False)

    

    class Meta:
        model = Profile
        fields = ['bio',
        'profile_pic',
        'phone',
        'website', 
        'facebook', 
        'instagram',
        'college',
        'school',
        ]
