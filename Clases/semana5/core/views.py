from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    mensaje = "<h1>Hola Mundo</h1>" 
   
    return HttpResponse(mensaje)
