"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('administrarcasas', views.listar_casas,
            name='listar_casas'),      
         path('administrardepartamentos', views.listar_departamentos,
            name='listar_departamentos'),      
        # Urls Casa
        path('casa/<int:id>', views.obtener_casa,
            name='obtener_casa'),        
        path('crear/casa', views.crear_casa,
            name='crear_casa'),
        path('editar_casa/<int:id>', views.editar_casa,
            name='editar_casa'),
        path('eliminar/casa/<int:id>', views.eliminar_casa,
            name='eliminar_casa'),
            
        # Urls Departamento
        
        path('departamento/<int:id>', views.obtener_departamento,
            name='obtener_departamento'),        
        path('crear/departamentos', views.crear_departamento,
            name='crear_departamento'),
        path('editar_departamento/<int:id>', views.editar_departamento,
            name='editar_departamento'),
        path('eliminar/departamento/<int:id>', views.eliminar_departamento,
            name='eliminar_departamento'),
        
       
 ]
