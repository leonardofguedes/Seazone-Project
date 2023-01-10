from django.db import models

class Imovel(models.Model):
    limite_hospedes = models.PositiveIntegerField()
    banheiros = models.PositiveIntegerField(default='1')
    animais = models.BooleanField(default=True)
    valor_limpeza = models.FloatField()
    data_ativacao = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

class Anuncio(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataforma = models.CharField(max_length=255)
    taxa_plataforma = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

class Reserva(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    preco_total = models.FloatField()
    comentario = models.CharField(max_length=255)
    hospedes = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
