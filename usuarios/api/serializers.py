from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id','last_login','is_superuser','is_active',
        'is_staff','groups','user_permissions','created_at',)

    def validate_password(self, value: str) -> str:
        """
            Hash value passed by user.

            :param value: password of a user
            :return: a hashed version of the password
        """
        return make_password(value)


class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'last_name', 'email','password','remember_password','username']
        read_only_fields = ('created_at',)

    def validate_password(self, value: str) -> str:
        """
            Hash value passed by user.

            :param value: password of a user
            :return: a hashed version of the password
        """
        return make_password(value)

    def validate_username(self, value: str) -> str:
        return self.name+"-"+self.last_name+value

class UsuarioTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
    # email = serializers.EmailField()
    # password = serializers.CharField()
    

    # @classmethod
    # def get_token(cls, usuario):
    #     token = {}

    #     # Add custom claims
    #     token['email'] = usuario.email
    #     token['password'] = usuario.password


    #     return token