from django.db import models


class Imovel(models.Model):
    codigo_imovel = models.CharField(max_length=200)
    limite_hospedes = models.IntegerField()
    quantidade_banheiros = models.IntegerField()
    aceita_animais = models.BooleanField(default=False)
    valor_limpeza = models.DecimalField(max_digits=8, decimal_places=2)
    data_ativacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
