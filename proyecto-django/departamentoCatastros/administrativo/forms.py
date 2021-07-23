from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Persona, Barrio, Casa, Departamento

# Form Persona
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese el nombre de la persona'),
            'direccion': _('Ingrese el apellido'),
            'cedula': _('Ingrese la cedula'),
            'correo': _('Ingrese el correo electrónico'),
        }

# Form Barrio   
class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']
        labels = {
            'nombre': _('Ingrese el nombre del barrio'),
            'siglas': _('Ingrese las siglas')
        }
    
  
# Form Departamento   
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio', 'valorBien', 'numCuartos', 'valorMantenimiento']
        labels = {
            'propietario': _('Seleccione el nombre del propietario'),
            'direccion': _('Ingrese la dirección'),
            'barrio': _('Seleccione el barrio al que pertenece'),
            'valorBien': _('Ingrese el valor del bien'),
            'numCuartos': _('Ingrese el numero de cuartos'),
            'valorMantenimiento': _('Ingrese el valor mensual del mantenimiento'),
        }


# Form Casa   
class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio', 'colorInmueble', 'valorBien', 'numCuartos', 'numPisos']
        labels = {
            'propietario': _('Seleccione el nombre del propietario'),
            'direccion': _('Ingrese la direccion'),
            'barrio': _('Seleccione el barrio al que pertenece'),
            'valorBien': _('Ingrese el valor del bien'),
            'colorInmueble': _('Ingrese el color del inmueble'),
            'numCuartos': _('Ingrese el numero de cuartos'),
            'numPisos': _('Ingrese la cantidad de pisos de la casa'),
        }