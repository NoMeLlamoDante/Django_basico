from django.db import models

# Create your models here.
class Curso(models.Model):
    descripcion = models.TextField()