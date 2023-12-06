from django.shortcuts import render, redirect
from .forms.registerform import NewUserForm
from .forms.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos, Proveedores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

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
        return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante,'es_admin': es_admin})

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

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ProveedorListView(AdminRequiredMixin, ListView):
    model = Proveedores
    template_name = 'proveedores.html'  # replace with your template name

class ProveedorCreateView(AdminRequiredMixin, CreateView):
    model = Proveedores
    template_name = 'add_proveedor.html'  # replace with your template name
    fields = ('nombre', 'telefono')  # replace with your Proveedor fields

class ProductoListView(AdminRequiredMixin, ListView):
    model = Productos
    template_name = 'productos.html'  # replace with your template name

class ProductoCreateView(AdminRequiredMixin, CreateView):
    model = Productos
    template_name = 'add_producto.html'  # replace with your template name
    fields = ('nombre', 'stock', 'fk_prov')  # replace with your Producto fields
