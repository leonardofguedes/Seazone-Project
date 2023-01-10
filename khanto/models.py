from django.db import models
from django.db.models import BigAutoField

class Imovel(models.Model):
    codigoImovel = models.BigAutoField(primary_key=True)
    limite_hospedes = models.PositiveIntegerField()
    banheiros = models.PositiveIntegerField(default='1')
    animais = models.BooleanField(default=True)
    valor_limpeza = models.FloatField()
    data_ativacao = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)


class Anuncio(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, db_constraint=False)
    plataforma = models.CharField(max_length=255)
    taxa_plataforma = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)


class Reserva(models.Model):
    codigoReserva = BigAutoField(primary_key=True)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    preco_total = models.FloatField()
    comentario = models.CharField(max_length=255)
    hospedes = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)
