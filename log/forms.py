from django import forms
from log import models 
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password','email')

#class UserProfileInfoForm(forms.ModelForm):
 #   class Meta():
  #      model = UserProfileInfo
   #     fields = ('portfoliosite','profile_pic')
        
