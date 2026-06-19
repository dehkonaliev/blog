from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post, Like, Comment

class CreatePost(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'create-post.html', {'form':form})
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.author = request.user
            posting.save()
            return redirect('profile')
        
        return render(request, 'create-post.html', {'form':form})


class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            like.delete()
            
        return redirect('home')