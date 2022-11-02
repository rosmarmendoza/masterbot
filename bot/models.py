from email.policy import default
from django.db import models

from usuarios.models import Usuario

# Create your models here.
class Bot(models.Model):
    name = models.CharField(max_length=30)
    token = models.CharField(max_length=30)
    welcome_message = models.TextField(default=f"Welcome: {Usuario.name} !!!")
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE) 