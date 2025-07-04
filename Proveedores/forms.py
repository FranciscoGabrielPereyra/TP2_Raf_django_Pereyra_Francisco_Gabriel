from django.forms import ModelForm
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'empresa', 'telefono', 'sitio_web','correo']