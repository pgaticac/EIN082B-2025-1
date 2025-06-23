from rest_framework import serializers
from core.models import Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"
        #fields = ["nombre","duracion"]
        #exclude = ["codigo"]