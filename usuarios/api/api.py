from usuarios.models import Usuario
from .serializers import UsuarioModelSerializer, UsuarioCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(http_method_names=['GET'])
def get_usuarios(request):
    usuarios = Usuario.objects.all()
    if len(usuarios) <= 0:
        return Response( data={"message":"No exiten datos"},status=status.HTTP_204_NO_CONTENT)

    usuarios_serializados = UsuarioModelSerializer(usuarios, many=True)
    return Response(usuarios_serializados.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def get_usuario(request, pk:int):
    usuario = Usuario.objects.filter(id=pk).first()
    if not usuario:
        return Response({"message":f"No existe el usuario con id:{pk}"}, status=status.HTTP_404_NOT_FOUND)
    usuario_serializado = UsuarioModelSerializer(usuario)
    return Response(usuario_serializado.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST'])
def create_usuario(request):
    usuario_serializado = UsuarioCreateSerializer(data=request.data)
    if usuario_serializado.is_valid():
        usuario_serializado.save()
        return Response({"message":"Usuario creado :)",
                        "data":usuario_serializado.data},
                         status=status.HTTP_201_CREATED)
    return Response(usuario_serializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['PUT','PATCH'])
def update_usuario(request, pk:int):
    usuario = Usuario.objects.filter(id=pk).first()
    if not usuario:
        return Response({"message": f"No existe el usuario con id:{pk}"}, status=status.HTTP_404_NOT_FOUND)    
    usuario_serializado = UsuarioModelSerializer(usuario,data=request.data)
    if usuario_serializado.is_valid():
        usuario_serializado.save()
        return Response({"message": "Usuario actualizado :)",
                        "data": usuario_serializado.data},
                       status=status.HTTP_200_OK)

    return Response(usuario_serializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['DELETE'])
def delete_usuario(request, pk: int):
    usuario = Usuario.objects.filter(id=pk).first()
    if not usuario:
        return Response({"message": f"No existe el usuario con id:{pk}"}, status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({"message":"se elimino el user"}, status=status.HTTP_200_OK)

    