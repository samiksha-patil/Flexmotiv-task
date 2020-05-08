from django import forms
from .models import Pic,Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title',)



class PicForm(forms.ModelForm):

    class Meta:
        model = Pic
        fields=('image',)
