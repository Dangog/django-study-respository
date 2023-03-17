from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome


# Create your models here.
class Receita(models.Model):
    titulo = models.CharField(max_length=65)

    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    dataCriacao = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    descricao = models.CharField(max_length=165)
    tempoPreparo = models.IntegerField()
    unidadeTempo = models.CharField(max_length=65)
    qtdPorcoes = models.IntegerField()
    passosPreparacao = models.TextField()
    estaPublicado = models.BooleanField(default=False)
    textoEmHTML = models.BooleanField(default=False)
    dataModificacao = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    capas = models.ImageField(upload_to='recipes/capas/%Y/%m/%d/', blank=True, default='')

    def __str__(self):
        return self.titulo
