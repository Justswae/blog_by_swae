from django import forms

from .models import Posts

class Create_form(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'post',
            'image',
            'author'
        ]