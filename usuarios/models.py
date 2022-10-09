from enum import unique
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, name, last_name, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = name+"_"+last_name,
            name=name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, name, last_name, email, password=None, **extra_fields):
        return self._create_user(name, last_name, email, password, False, False, **extra_fields)

    def create_superuser(self, name, last_name, email, password=None, **extra_fields):
        return self._create_user( name, last_name, email, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    remember_password = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']
    
    def __str__(self):
        return f'Usuario/ {self.name} {self.last_name}'