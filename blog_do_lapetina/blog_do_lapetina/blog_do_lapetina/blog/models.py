from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)