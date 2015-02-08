from django.forms import *
from openapp.models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['owner', 'name', 'desc', 'lang', 'source']