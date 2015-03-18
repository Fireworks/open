import datetime
from haystack import indexes
from openapp.models import Code, Project

class CodeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    language = indexes.IntegerField(model_attr='language__id')
    description = indexes.CharField(model_attr='description')
    rating = indexes.IntegerField(model_attr='rating')
    
    def get_model(self):
        return Code

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects

class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    language = indexes.IntegerField(model_attr='language__id')
    description = indexes.CharField(model_attr='description')
    rating = indexes.IntegerField(model_attr='rating')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects