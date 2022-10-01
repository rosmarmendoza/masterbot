from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets, permissions

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer