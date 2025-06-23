from django.shortcuts import render
from rest_framework import viewsets
from core.models import Carrera
from .serializers import CarreraSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    #filtrado de la data
    serializer_class = CarreraSerializer