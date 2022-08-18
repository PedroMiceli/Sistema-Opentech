from django.db import models

# Create your models here.

class Contato(models.Model):
    email = models.CharField(max_length=50)
    mensagem = models.CharField(max_length=150)
