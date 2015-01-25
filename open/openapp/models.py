from django.db import models
from django.conf import settings

class DatedMixin(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(DatedMixin, models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    lang = models.CharField(max_length=25)
    source = models.URLField()
