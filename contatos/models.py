from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25, blank=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='fotos', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.nome


