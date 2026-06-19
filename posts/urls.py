from django.urls import path
from .views import CreatePost, LikeView

urlpatterns = [
    path('create', CreatePost.as_view(), name='create-post'),
    path('like/<int:pk>', LikeView.as_view(), name='like')
]