# contains form built by us

from django import forms
from django.contrib.auth.models import User   #this is inbuilt not our user
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    #meta class is class which prvide info about itself
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
