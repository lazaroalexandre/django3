
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=300, verbose_name='Nome')
    descricao = models.CharField(max_length=500, verbose_name='Descrição')
    def __str__(self):
        return f"{self.nome} ({self.descricao})"

class MeusProjetos(models.Model):
    assunto = models.CharField(verbose_name="Assunto", max_length=300)
    descricao = models.TextField(
        verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    campo = models.ForeignKey(
        User, on_delete=models.PROTECT)  # chave estrangeira
    def __str__(self):
        return f"{self.assunto} ({self.campo})?"

class Relatorios(models.Model):
    assunto = models.CharField(
        verbose_name="Assunto", max_length=300)
    descricao = models.TextField(
        verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    campo = models.ForeignKey(User, on_delete=models.PROTECT) #chave estrangeira
    def __str__(self):
        return f"{self.assunto} ({self.campo})?"

class Ideias(models.Model):
    assunto = models.CharField(verbose_name="Assunto", max_length=300)
    descricao = models.TextField(
        verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    campo = models.ForeignKey(User, on_delete=models.PROTECT) #chave estrangeira
    def __str__(self):
        return f"{self.assunto} ({self.campo})?"

class Atividades(models.Model):
    assunto = models.CharField(verbose_name="Assunto", max_length=300)
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    campo = models.ForeignKey(
        User, on_delete=models.PROTECT)  # chave estrangeira

    def __str__(self):
        return f"{self.assunto} ({self.campo})?"


class Conquistas(models.Model):
    assunto = models.CharField(verbose_name="Assunto", max_length=300)
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    campo = models.ForeignKey(
        User, on_delete=models.PROTECT)  # chave estrangeira

    def __str__(self):
        return f"{self.assunto} ({self.campo})?"
