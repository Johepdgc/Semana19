"""S19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appOne import views as appone
from appOne.views import ProveedorListView, ProveedorCreateView, ProductoListView, ProductoCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appone.index, name='home'),
    path('registro/', appone.reg_user),
    path('login/', appone.iniciar_sesion, name='login'),
    path('logout/', appone.cerrar_sesion, name='logout'),
    path('proveedores/', ProveedorListView.as_view(), name='proveedores'),
    path('add_proveedor/', ProveedorCreateView.as_view(), name='add_proveedor'),
    path('productos/', ProductoListView.as_view(), name='productos'),
    path('add_producto/', ProductoCreateView.as_view(), name='add_producto'),
    path('proveedores/<int:pk>/', ProveedorListView.as_view(), name='proveedores-detail'),
    path('productos/<int:pk>/', ProductoListView.as_view(), name='productos-detail'),
]
