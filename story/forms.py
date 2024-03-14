from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'author','featured_image', 'content','excerpt',
        'status','pinned']