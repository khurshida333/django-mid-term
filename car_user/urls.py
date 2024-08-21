from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register,name='Register'),
    # path('login/', views.user_login,name='Login'),
    path('login/', views.UserLogInView.as_view(),name='Login'),
    # path('login/', auth_views.LoginView.as_view(),name='Login'),
    path('logout/', views.user_logout,name='Logout'),
    # path('logout/', LogoutView.as_view(next_page='Login'), name='Logout'),
    path('profile/', views.profile,name='Profile'),
    path('profile/edit', views.edit_profile,name='Edit_profile'),
    path('profile/edit/change_password/', views.change_pass,name='Change_pass'),
]
