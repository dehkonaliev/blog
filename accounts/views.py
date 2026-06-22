from http.client import HTTPResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,  UserUpdateForm, UserForm
from posts.models import Post
from .utils import send_test_email, send_test_email_login
from django.contrib.auth import get_user_model


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            send_test_email_login(user.email)
            return redirect('home')
        
        return render(request, 'login.html', {'form':form})
    
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.filter(author=request.user)
        return render(request, 'profile.html', {'posts':posts})


class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'signup.html', {'form':form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            send_test_email(user.email)
            return redirect('profile')
        return render(request, 'signup.html', {'form':form})








class UserUpdateView(View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, 'update.html', {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'update.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('home')



class UserDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'delete.html')

    def post(self, request):
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')

        posts = Post.objects.filter(author=request.user).order_by('-id')
        return render(request, 'profile.html', {'posts':posts})
    
    
class UserProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        posts = Post.objects.filter(author=user)
        
        return render(request, 'user-profile.html', {'user':user, 'posts':posts})
        



