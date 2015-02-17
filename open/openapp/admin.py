from django.contrib import admin
from openapp.models import *

class UserAdmin(admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    pass

class CodeAdmin(admin.ModelAdmin):
    pass

class CodeCommentAdmin(admin.ModelAdmin):
    pass

class CodeFeedbackAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class ProjectCommentAdmin(admin.ModelAdmin):
    pass

class ProjectFeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(CodeComment, CodeCommentAdmin)
admin.site.register(CodeFeedback, CodeFeedbackAdmin)
admin.site.register(ProjectComment, ProjectCommentAdmin)
admin.site.register(ProjectFeedback, ProjectFeedbackAdmin)