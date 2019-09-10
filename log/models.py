# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
#return value
def __str__(self):
    return self.user.username
    
class department (models.Model):
    dept = models.CharField(max_length=30)

    def __str__(self):
        return self.dept

class ticket (models.Model):
    Date = models.DateField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Dept = models.ForeignKey(department, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=60)
    Details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Subject


class users (models.Model):
    UserName = models.CharField(max_length=20, null=False,unique=True)
    Name= models.CharField(max_length=20)
    Email = models.EmailField(max_length=70, blank=True)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
