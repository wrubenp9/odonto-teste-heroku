from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthForm

from .forms import RegisterUserForm
from .forms import PasswordResetForm


def register(request):
    template_name = 'register.html'
    form = RegisterUserForm(data=request.POST or None)
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
    
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = RegisterUserForm()
        messages.success(request, 'erro ao cadastrar!')
        
    context = {
        'form': form
    }
    return render(request, template_name, context)


def login(request):
    template_name = 'login.html'
    
    # Se estiver logado, não entra no login.html
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username,  password=password)
    
        if usuario is not None:
            auth_login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,'Erro ao logar!')
            form_login = CustomAuthForm()
    else:
        form_login = CustomAuthForm()

    context = {
        'form': form_login
    }
    return render(request, template_name, context)

def password_reset(request):
    template_name = 'password_reset.html'
    form = PasswordResetForm()

