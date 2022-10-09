import imp
from django.urls import path
from .api import get_usuarios, get_usuario,create_usuario,\
    update_usuario,delete_usuario

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.views import MyTokenObtainPairView

urlpatterns=[
    path('user/list', get_usuarios, name='list_users'),
    path('user/list/<pk>', get_usuario, name='list_user'),
    path('user/create', create_usuario, name='create_user'),
    path('user/update/<pk>', update_usuario, name='update_user'),
    path('user/delete/<pk>', delete_usuario, name='delete_user'),

    path('user/auth', MyTokenObtainPairView.as_view(), name='auth_user_view'),

]