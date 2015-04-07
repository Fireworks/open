from django.forms import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from openapp.models import *
from haystack.forms import ModelSearchForm
from haystack.inputs import Exact, Raw

class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = ['name', 'language', 'description', 'source']

class ProjectCommentForm(ModelForm):
    
    class Meta:
        model = ProjectComment
        fields = ['text']

class ProjectFeedbackForm(ModelForm):
    
    class Meta:
        model = ProjectFeedback
        fields = ['text']

class CodeForm(ModelForm):

    class Meta:
        model = Code
        fields = ['name', 'language', 'description', 'source']

class CodeCommentForm(ModelForm):
    
    class Meta:
        model = CodeComment
        fields = ['text']
        
class CodeFeedbackForm(ModelForm):
    
    class Meta:
        model = CodeFeedback
        fields = ['text']

class BasicSearchForm(ModelSearchForm):
    q = forms.CharField(required=True, label=('Name'))
    languages = Language.objects.all()
    language_options = tuple([(l.id, l.name) for l in languages])
    language = forms.ChoiceField(required=False, choices=language_options)

    def search(self):
        sqs = super(BasicSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()
        
        if self.cleaned_data['language']:
            sqs = sqs.filter(language=self.cleaned_data['language'])
            
        sqs = sqs.order_by('-rating')
        
        return sqs
