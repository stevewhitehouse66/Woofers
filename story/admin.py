from django.contrib import admin
from .models import Story
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):

    list_display = ('title',  'status', 'created_on')
    search_fields = ['title','content']
    list_filter = ('status',)
    summernote_fields = ('content')