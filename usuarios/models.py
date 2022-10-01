from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    remember_password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)