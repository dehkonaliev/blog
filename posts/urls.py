from django.urls import path
from .views import CreatePost

urlpatterns = [
    path('create', CreatePost.as_view(), name='create-post')
]