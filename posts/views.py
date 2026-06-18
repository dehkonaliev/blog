from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

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