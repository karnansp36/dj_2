from django.db import models
from django.contrib import admin
# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField()
    
admin.site.register(Signup)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
