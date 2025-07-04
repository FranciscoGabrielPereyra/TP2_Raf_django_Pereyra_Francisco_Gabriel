from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.Listar_Proveedores, name='Listar_Proveedores'),
    path('crear/', views.crear_proveedores, name='crear_proveedores'),
    path('editar/<int:id>/', views.editar_proveedores, name='editar_proveedores'),
    path('eliminar/<int:id>/', views.eliminar_proveedores, name='eliminar_proveedores'),
    path('', views.principal, name='principal'),
]

