from django.forms import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from openapp.models import Project, Code, Language
from haystack.forms import ModelSearchForm
from haystack.inputs import Exact, Raw

class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = ['name', 'description', 'language', 'source']

class CodeForm(ModelForm):

    class Meta:
        model = Code
        fields = ['name', 'language', 'description', 'source']

class BasicSearchForm(ModelSearchForm):
    q = forms.CharField(required=True, label=('Name'))
    languages = Language.objects.all()
    language_options = tuple([(l.id, l.name) for l in languages])
    language = forms.ChoiceField(required=False, choices=language_options)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(BasicSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()
        
         # Check to see if a start_date was chosen.
        if self.cleaned_data['language']:
            sqs = sqs.filter(language=self.cleaned_data['language'])
        return sqs
