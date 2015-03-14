from django.forms import *
from django import forms
from openapp.models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'language', 'source']
