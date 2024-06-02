from rest_framework import serializers
from .models import Usuario

# serializer para Usuario:
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'