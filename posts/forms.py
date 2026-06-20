from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'body', 'image', 'category']
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=1, max_length=1000)
    class Meta:
        model = Comment
        fields = ['content']