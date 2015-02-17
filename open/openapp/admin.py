from django.contrib import admin
from openapp.models import *

class UserAdmin(admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    pass

class CodeAdmin(admin.ModelAdmin):
    pass

#class ProjectAdmin(admin.ModelAdmin):
#    pass

class CommentCodeAdmin(admin.ModelAdmin):
    pass

class FeedbackCodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Code, CodeAdmin)
#admin.site.register(Project, ProjectAdmin)
admin.site.register(CommentCode, CommentCodeAdmin)
admin.site.register(FeedbackCode, FeedbackCodeAdmin)