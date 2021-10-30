from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    # path('register/', auth_views.SignUp.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]