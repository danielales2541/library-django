from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Users(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)

    