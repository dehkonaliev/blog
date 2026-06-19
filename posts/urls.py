from django.urls import path
from .views import CreatePost, LikeView, PostDetailView, CommentView

urlpatterns = [
    path('create', CreatePost.as_view(), name='create-post'),
    path('like/<int:pk>', LikeView.as_view(), name='like'),
    path('detailed/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>', CommentView.as_view(), name='comment'),
]