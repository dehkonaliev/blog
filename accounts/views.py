from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,  UserUpdateForm, UserForm
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
<<<<<<< HEAD
        posts = Post.objects.filter(author=request.user)
        return render(request, 'profile.html', {'posts':posts})


class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'signup.html', {'form':form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        return render(request, 'signup.html', {'form':form})


class UserUpdateView(View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, 'update.html', {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
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

=======
        posts = Post.objects.filter(author=request.user).order_by('-id')
        return render(request, 'profile.html', {'posts':posts})
>>>>>>> origin
