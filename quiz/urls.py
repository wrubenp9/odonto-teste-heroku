from django.urls import path
from . import views

# Create your views here.

app_name = 'quiz'
urlpatterns = [
    path('forms/', views.forms, name='forms')
]
