from django.shortcuts import render
from django.views import View
from posts.models import Post

class HomeView(View):
    def get(self, request):
        posts = Post.objects.order_by('-id')[:6]
        return render(request, 'index.html', {'posts':posts})
    

