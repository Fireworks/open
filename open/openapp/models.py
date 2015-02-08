from django.db import models
from django.conf import settings

class DatedMixin(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(DatedMixin, models.Model):
    LANGUAGES = (
        ('Python', 'Python'),
        ('Javascript', 'Javascript'),
        ('Java', 'Java'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    lang = models.CharField(max_length=25, choices=LANGUAGES)
    source = models.URLField(blank=True)

    def get_absolute_url(self):
        return "/project/%i/" % self.id