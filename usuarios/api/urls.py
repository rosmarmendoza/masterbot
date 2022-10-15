import imp
from django.urls import path
from .api import get_usuarios, get_usuario,create_usuario,\
    update_usuario,delete_usuario

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.views import MyTokenObtainPairView
#para recuperar el password
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns=[
    #api rest de usuairos
    path('list', get_usuarios, name='list_users'),
    path('list/<pk>', get_usuario, name='list_user'),
    path('create', create_usuario, name='create_user'),
    path('update/<pk>', update_usuario, name='update_user'),
    path('delete/<pk>', delete_usuario, name='delete_user'),

    #para obtener los tokens de auth y refresh cuando de loguea
    path('auth', MyTokenObtainPairView.as_view(), name='auth_user_view'),
    
    #para resetear el password, mediante el envio de emails
    path('recover-password/', PasswordResetView.as_view(), name='password_reset'),
    path('recover-password-send/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('recover-password/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('recover-password-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]