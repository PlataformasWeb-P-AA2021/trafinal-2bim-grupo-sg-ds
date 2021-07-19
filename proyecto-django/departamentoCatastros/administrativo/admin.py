from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Barrio, Persona, Casa, Departamento

# Register your models here.

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre', 'siglas')
admin.site.register(Barrio, BarrioAdmin)    


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','cedula', 'correo')
    search_fields = ('nombre', 'cedula')    
admin.site.register(Persona, PersonaAdmin)    


class CasaAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion','barrio', 'valorBien','colorInmueble', 'numCuartos', 'numPisos')
    search_fields = ('nombre', 'cedula')  
admin.site.register(Casa, CasaAdmin)   
 

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion','barrio', 'valorBien','numCuartos', 'valorMantenimiento')
    search_fields = ('nombre', 'cedula')     
admin.site.register(Departamento, DepartamentoAdmin)    