from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200,)
    author = models.CharField(max_length=100)
    aviableCopies = models.IntegerField(default=0)