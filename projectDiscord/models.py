from django.db import models

class UserLogIn(models.Model):
    name = models.CharField(max_length=30)
    