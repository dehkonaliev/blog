from django.urls import path
from .views import LoginView, ProfileView, UserUpdateView, SignUpView,  logout_view, UserDeleteView, UserProfileView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('user', UserUpdateView.as_view(), name='user'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', logout_view, name='logout'),
    path('user_delete', UserDeleteView.as_view(), name='user_delete'),
    path('users/<slug:username>', UserProfileView.as_view(), name='user-profile')

]