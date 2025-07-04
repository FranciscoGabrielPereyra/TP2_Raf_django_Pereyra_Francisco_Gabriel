from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm

def Listar_Proveedores(request):
    proveedor = Proveedor.objects.all()
    return render(request, "proveedores.html", {"proveedores": proveedor})

def crear_proveedores(request):
    if request.method == 'GET':
        return render(request, 'crear_proveedores.html', {
            'form': ProveedorForm
        })
    else:
        try:
            form = ProveedorForm(request.POST)
            nuevo_producto = form.save(commit=False)
            nuevo_producto.save()
            return redirect('/listar')
        except ValueError:
            return render(request, 'crear_proveedores.html', {
                'form': ProveedorForm,
                'error': 'Por favor ingrese datos válidos'
            })

def editar_proveedores(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.apellido = request.POST['apellido']
        proveedor.correo = request.POST['correo']
        proveedor.telefono = request.POST['telefono']
        proveedor.empresa = request.POST['empresa']
        proveedor.sitio_web = request.POST['sitio_web']
        proveedor.save()
        return redirect('Listar_Proveedores')
    return render(request, 'editar_proveedores.html', {'proveedor': proveedor})


def eliminar_proveedores(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('Listar_Proveedores')
    return render(request, 'eliminar_proveedores.html', {'proveedor': proveedor})

def principal(request):
    return render(request, 'principal.html')