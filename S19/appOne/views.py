from django.shortcuts import render, redirect
from .forms.registerform import NewUserForm
from .forms.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos, Proveedores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def reg_user(request):
    if request.method == 'POST':
        forms = NewUserForm(request.POST)
        if forms.is_valid():
            forms.save()
        return HttpResponseRedirect('/')
    else:
        forms = NewUserForm()
        return render(request, 'Reg_user.html', {'form': forms})

@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user': request.user})

def iniciar_sesion(request):
    if request.method == 'POST':
        forms = LoginForm(request, data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        forms = LoginForm()
    return render(request, 'login.html', {'form': forms})
    
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

