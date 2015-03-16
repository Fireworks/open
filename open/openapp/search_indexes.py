import datetime
from haystack import indexes
from openapp.models import Code, Project

class CodeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    language = indexes.CharField(model_attr='language')
    description = indexes.CharField(model_attr='description')
    
    def get_model(self):
        return Code

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects

class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    language = indexes.CharField(model_attr='language')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects