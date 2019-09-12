from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    fields = ('author', ('min_mark', 'max_mark', 'difficulty', 'date'),
              'question_type', 'question', 'topic')

    fields = ('author', ('min_mark', 'max_mark', 'difficulty', 'date'),
              'topic', 'questionType', 'question',)

    list_display = ('question_trim', 'mark_range',
                    'difficulty', 'questionType', 'get_topics', 'author')

    search_fields = ('question_trim', 'difficulty',
                     'questionType', 'get_topics' 'author')


admin.site.register(Topic)
admin.site.register(Type)
admin.site.register(Question, OrderAdmin)
