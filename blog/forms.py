
from django import forms
  
# import GeeksModel from models.py
from .models import Post
  
# create a ModelForm
class PostForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }