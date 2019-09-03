from django.contrib import admin
from .models import *


class SnippetAdmin(admin.ModelAdmin):
    change_list_template = 'admin/questions/login.html'


admin.site.register(Topic, SnippetAdmin)
admin.site.register(Type, SnippetAdmin)
