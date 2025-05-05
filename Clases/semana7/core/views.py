from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

def home(request):
    titulo = 'Hola Mundo'
    data ={
        "titulo" : titulo,
    }

    return render(request,'core/index.html', data)

def carreras(request):
    titulo = 'Carreras'
    
    lista_carreras = Carrera.objects.all()

    data ={
        "titulo" : titulo,
        "carreras" : lista_carreras,
    }
    return render(request,'core/carreras.html',data)

def docentes(request):
    return render(request,'core/docentes.html')

def contacto(request):
    return render(request,'core/contacto.html')