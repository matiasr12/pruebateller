from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombreap = models.CharField(max_length=255)
    apellidoap = models.CharField(max_length=255)
    # Otros campos personalizados que quieras guardar para el Profesor

    def __str__(self):
        return self.user.username
    



class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    # Otros campos personalizados que quieras guardar para el Estudiante

    def __str__(self):
        return f"{self.first_name} {self.last_name}"