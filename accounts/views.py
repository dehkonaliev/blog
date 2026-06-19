from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm
from posts.models import Post


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('home')
        
        return render(request, 'login.html', {'form':form})
    
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.filter(author=request.user).order_by('-id')
        return render(request, 'profile.html', {'posts':posts})