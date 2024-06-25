from rest_framework import serializers
from .models import *

# LO UTILIZAMOS PARA TRANSFORMAR PYTHON A JSON
class TipoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpleado
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    tipo = TipoEmpleadoSerializer(read_only=True)
    class Meta:
        model = Empleado
        fields = '__all__'