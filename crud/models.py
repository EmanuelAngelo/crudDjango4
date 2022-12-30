from django.db import models

# Create your models here.
class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('femenino', 'Femenino'),
        ('masculino', 'Masculino'),
    )
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES, default='masculino')