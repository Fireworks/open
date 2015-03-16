from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from openapp.models import Project, Code
from haystack.forms import ModelSearchForm
from haystack.inputs import Exact, Raw

class BasicSearchForm(ModelSearchForm):
    q = forms.CharField(required=True, label=('Name'))
    language = forms.CharField(required=False)

    class Meta:
        model = Project
        fields = ['name', 'description', 'language', 'source']

class CodeForm(ModelForm):

    class Meta:
        model = Code
        fields = ['name', 'language', 'description', 'source']


    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(BasicSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()
        
         # Check to see if a start_date was chosen.
        if self.cleaned_data['language']:
            sqs = sqs.filter(language__name__exact=self.cleaned_data['language'])
        return sqs
