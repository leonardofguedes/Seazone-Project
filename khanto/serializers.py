from rest_framework import serializers
from .models import Imovel, Anuncio, Reserva

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('id', 'codigoImovel', 'limite_hospedes', 'banheiros', 'animais', 'valor_limpeza', 'data_ativacao', 'data_criacao', 'data_atualizacao')

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ('id', 'imovel', 'plataforma', 'taxa_plataforma', 'data_criacao', 'data_atualizacao')

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('id', 'anuncio', 'checkin', 'checkout', 'preco_total', 'comentario', 'hospedes', 'data_criacao', 'data_atualizacao')