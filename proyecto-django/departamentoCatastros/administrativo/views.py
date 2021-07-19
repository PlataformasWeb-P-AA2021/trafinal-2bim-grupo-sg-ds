from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, \
    PersonaSerializer, CasaSerializer, DepartamentoSerializer, BarrioSerializer

def index(request):    
    return render(request, 'index.html')

# Métodos Login

def ingreso(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

# listar casas y departamentos
def listar_casas(request):
    casas = Casa.objects.all()    
    informacion_template = {'casas': casas}
    return render(request, 'listar_casas.html', informacion_template)

def listar_departamentos(request):
    departamentos = Departamento.objects.all()    
    informacion_template = {'departamentos': departamentos}
    return render(request, 'listar_departamentos.html', informacion_template)


# Crud Casas
def obtener_casa(request, id):  
    casa = Casa.objects.get(pk=id)
    informacion_template = {'casa': casa}
    return render(request, 'obtener_casa.html', informacion_template)

def crear_casa(request): 
    if request.method=='POST':
        formulario = CasaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(listar_casas)
    else:
        formulario = CasaForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crear_casa.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.change_casa', login_url="/entrando/login/")
def editar_casa(request, id):
    casa = Casa.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaForm(request.POST, instance=casa)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_casas)
    else:
        formulario = CasaForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_casa.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.delete_casa', login_url="/entrando/login/")
def eliminar_casa(request, id):
    casa = Casa.objects.get(pk=id)
    casa.delete()
    return redirect(index)


# Crud Departamentos
def obtener_departamento(request, id):  
    departamento = Departamento.objects.get(pk=id)
    informacion_template = {'departamento': departamento}
    return render(request, 'obtener_departamento.html', informacion_template)

def crear_departamento(request): 
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(listar_departamentos)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crear_departamento.html', diccionario)


@login_required(login_url='/entrando/login/')
@permission_required('administrativo.change_departamento', login_url="/entrando/login/")
def editar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_departamentos)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}
    return render(request, 'editar_departamento.html', diccionario)


@login_required(login_url='/entrando/login/')
@permission_required('administrativo.delete_departamento', login_url="/entrando/login/")
def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

# Vistas restframework
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

class BarriosViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CasasViewSet(viewsets.ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]