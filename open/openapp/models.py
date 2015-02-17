from django.db import models
from django.conf import settings
from django.template.defaultfilters import truncatechars

class DatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(DatedMixin, models.Model):
    first_name  = models.CharField(max_length=15, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name   = models.CharField(max_length=25, blank=True)
    username    = models.CharField(max_length=15, unique=True)
    password    = models.CharField(max_length=25)
    email       = models.EmailField(max_length=50)
    
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
    comments    = models.ManyToManyField(User, related_name='code_comments', through='CodeComment')
    feedback    = models.ManyToManyField(User, related_name='code_feedback', through='CodeFeedback')
    language    = models.ForeignKey(Language)
    name        = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    source      = models.TextField()
    rating      = models.IntegerField(blank=True, default=0)
    
    class Meta:
        verbose_name_plural = 'Code'
    
    def short_description(self):
        return truncatechars(self.description, 100)
    
    def __unicode__(self):
        return (self.name)

class CodeComment(DatedMixin, models.Model):
    user        = models.ForeignKey(User)
    code        = models.ForeignKey(Code)
    text        = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Code Comments'
        
    def short_text(self):
        return truncatechars(self.text, 100)
        
    def __unicode__(self):
        return (self.text)
    
class CodeFeedback(DatedMixin, models.Model):
    user        = models.ForeignKey(User)
    code        = models.ForeignKey(Code)
    text        = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Code Feedback'
    
    def short_text(self):
        return truncatechars(self.text, 100)
    
    def __unicode__(self):
        return (self.text)
    
class Project(DatedMixin, models.Model):
    users       = models.ManyToManyField(User, related_name='project_users')
    comments    = models.ManyToManyField(User, related_name='project_comments', through='ProjectComment')
    feedback    = models.ManyToManyField(User, related_name='project_feedback', through='ProjectFeedback')
    language    = models.ForeignKey(Language, null=True)
    name        = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    source      = models.URLField(blank=True)
    rating      = models.IntegerField()
    
    def short_description(self):
        return truncatechars(self.description, 100)
    
    def __unicode__(self):
        return (self.name + ' ' + self.language)

class ProjectComment(DatedMixin, models.Model):
    user        = models.ForeignKey(User)
    project     = models.ForeignKey(Project)
    text        = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Project Comments'
    
    def short_text(self):
        return truncatechars(self.text, 100)
    
    def __unicode__(self):
        return (self.text)
    
class ProjectFeedback(DatedMixin, models.Model):
    user        = models.ForeignKey(User)
    project     = models.ForeignKey(Project)
    text        = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Project Feedback'
    
    def short_text(self):
        return truncatechars(self.text, 100)
    
    def __unicode__(self):
        return (self.text)
