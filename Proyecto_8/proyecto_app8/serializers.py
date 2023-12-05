from rest_framework import serializers
from proyecto_app8 import models

class EstudianteSerial(serializers.ModelSerializer):
    class Meta:
        models = models.Estudiante
        fields = '__all__'