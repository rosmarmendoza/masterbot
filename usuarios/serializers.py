from dataclasses import fields
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'name', 'lastname', 'email', 'password', 'remember_password', 'created_at')
        read_only_fields = ('created_at',)