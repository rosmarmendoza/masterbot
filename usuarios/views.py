from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .api.serializers import UsuarioTokenObtainPairSerializer, UsuarioModelSerializer

from .models import Usuario
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsuarioTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):

        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(
            email=email,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UsuarioModelSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'datos incorrectos :(', "err": login_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'el usario con estas credenciales no existe'}, status=status.HTTP_400_BAD_REQUEST)