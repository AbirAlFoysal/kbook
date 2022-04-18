from distutils.text_file import TextFile
import profile
from django.utils import timezone
from pickle import TRUE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.urls import reverse
from user.models import Profile

# Create your models here.

# class Post(models.Model):
#     author = models.ForeignKey(Profile , on_delete=models.CASCADE)
#     title = models.TextField(max_length= 500)

#     def __str__(self):
#         return self.author



class book(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('bookdetail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()
