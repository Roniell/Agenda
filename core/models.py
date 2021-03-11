from django.db import models

from django.contrib.auth.models import User


class Agenda(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    telefone = models.CharField(max_length=20, blank=False, verbose_name='número de telefone')
    email = models.EmailField(max_length=200, blank=False)
    endereco = models.CharField(max_length=250, blank=False, verbose_name='endereço')
    bairro = models.CharField(max_length=100, blank=False)
    cep = models.CharField(max_length=9, blank=False)
    cidade = models.CharField(max_length=150, blank=False)
    data_add = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
