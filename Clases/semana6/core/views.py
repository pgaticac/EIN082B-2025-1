from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    titulo = 'Hola Mundo'
    data ={
        "titulo" : titulo,
    }

    return render(request,'core/index.html', data)

def carreras(request):
    titulo = 'Carreras'

    lista_carreras = list()
    lista_carreras.append("Ingeniería en Informática")
    lista_carreras.append("Técnico Universitario en Informática")
    lista_carreras.append("Técnico Universitario en Ciencia de Datos")
    lista_carreras.append("Ingeniería de Ejecución en Software")
    lista_carreras.append("Ingeniería Civil Informática")

    data ={
        "titulo" : titulo,
        "carreras" : lista_carreras,
    }
    return render(request,'core/carreras.html',data)

def docentes(request):
    return render(request,'core/docentes.html')

def contacto(request):
    return render(request,'core/contacto.html')