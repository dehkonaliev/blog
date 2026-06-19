from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
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
            
        next_page = request.META.get('HTTP_REFERER')
        
        if next_page:
            return redirect(next_page)
        
        return redirect('home')
    
class PostDetailView(View):
    def get(self, request, pk):
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post).all()
        return render(request, 'post-detail.html', {'post':post, 'comments':comments, 'form':form})
    
    
class CommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm()
        return render(request, 'post-detail.html', {'post':post, 'form':form})
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            add_comment = form.save(commit=False)
            add_comment.author = request.user
            add_comment.post = post
            add_comment.save()
            
        next_page = request.META.get('HTTP_REFERER')
        if next_page:
            return redirect(next_page)
        
        return redirect('home')
    
class PostUpdateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'post-update.html', {'form':form})
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            
            return redirect('post-detail', pk=post.pk)
                    
        return render(request, 'post-update.html', {'form':form})
    
class PostDeleteView(View):
    pass

