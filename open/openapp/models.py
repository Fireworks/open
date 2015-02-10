from django.db import models
from django.conf import settings

class DatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(DatedMixin, models.Model):
    first_name  = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name   = models.CharField(max_length=25)
    username    = models.CharField(max_length=15, unique=True)
    password    = models.CharField(max_length=25)
    email       = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.username
    
class Language(DatedMixin, models.Model):
    name        = models.CharField(max_length=20)
    version     = models.CharField(max_length=10, blank=True)
    
    class Meta:
        unique_together = ('name', 'version')
        
    def __unicode__(self):
        return (self.name + ' ' + self.version)
        
    
class Code(DatedMixin, models.Model):
    users       = models.ManyToManyField(User, related_name='code_users')
    comments    = models.ManyToManyField(User, related_name='code_comments', through='CommentCode')
    feedback    = models.ManyToManyField(User, related_name='code_feedback', through='FeedbackCode')
    language    = models.ForeignKey(Language)
    name        = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    source      = models.TextField()
    rating      = models.IntegerField()
    
    def __unicode__(self):
        return (self.name + ': ' + self.description)

class CommentCode(DatedMixin, models.Model):
    user        = models.ForeignKey(User)
    code        = models.ForeignKey(Code)
    text        = models.TextField()
    
class FeedbackCode(DatedMixin, models.Model):
    user        = models.ForeignKey(User)
    code        = models.ForeignKey(Code)
    text        = models.TextField()

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
    
#class Project(DatedMixin, models.Model):
#    users       = models.ManyToManyField(User, related_name='project_users')
#    comments    = models.ManyToManyField(User, related_name='project_comments', through='CommentProject')
#    feedback    = models.ManyToManyField(User, related_name='project_feedback', through='FeedbackProject')
#    language    = models.ForeignKey(Language)
#    name        = models.CharField(max_length=20)
#    description = models.TextField(blank=True)
#    source      = models.URLField(blank=True)
#    rating      = models.IntegerField()
#    
#    def __unicode__(self):
#        return (self.name + ' ' + self.language)
#
#class CommentProject(DatedMixin, models.Model):
#    user        = models.ForeignKey(User)
#    code        = models.ForeignKey(Code)
#    text        = models.TextField()
#    
#class FeedbackProject(DatedMixin, models.Model):
#    user        = models.ForeignKey(User)
#    code        = models.ForeignKey(Code)
#    text        = models.TextField()
