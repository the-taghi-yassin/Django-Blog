from django import forms
from .models import *


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False
    class Meta:
        model = Post
        fields = ['category','book_author', 'title','description', 'content', 'tags', 'status']
        labels = {'book_author':"", 'title':"",'description':"", 'category':"", 'tags':"", 'status':""}

        widgets= {
            'book_author':forms.TextInput(attrs={'class':'form-control','placeholder':'Book Author','style': 'box-shadow: none'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title','style': 'box-shadow: none'}),
            'description':forms.Textarea(attrs={'rows': 4,'class':'form-control','placeholder':'description','style': 'box-shadow: none'}),
            'tags':forms.TextInput(attrs={'class':'form-control','placeholder':'tags','style': 'box-shadow: none'}),
            }