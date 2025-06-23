from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

def home(request):
    titulo = 'Hola Mundo'
    data ={
        "titulo" : titulo,
    }

    return render(request,'core/index.html', data)

def carreras(request,id=0):
    titulo = 'Carreras'

    if(request.POST):
        #capturar datos desde form
        codigo = request.POST["txtCodigo"]
        nombre = request.POST["txtNombre"]
        duracion = int(request.POST["txtDuracion"])

        #validaciones

        nuevaCarrera = Carrera()
        nuevaCarrera.codigo = codigo
        nuevaCarrera.nombre = nombre
        nuevaCarrera.duracion = duracion

        nuevaCarrera.save()
    
    if id != 0:
        carrera = Carrera.objects.get(id=id)
        carrera.delete()

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