from django.forms import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from openapp.models import Project, Code

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'language', 'source']

class CodeForm(ModelForm):

    class Meta:
        model = Code
        fields = ['name', 'language', 'description', 'source']

# class RegisterForm(UserCreationForm)
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password']
        
