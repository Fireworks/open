from django.contrib import admin
from openapp.models import *

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'language', 'created', 'edited')

@admin.register(CodeComment)  
class CodeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'short_text', 'created', 'edited')

@admin.register(CodeFeedback)
class CodeFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'short_text', 'created', 'edited')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'language', 'created', 'edited')

@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'short_text', 'created', 'edited')

@admin.register(ProjectFeedback)
class ProjectFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'short_text', 'created', 'edited')