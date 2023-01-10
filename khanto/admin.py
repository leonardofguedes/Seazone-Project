from django.contrib import admin
from .models import Imovel, Anuncio, Reserva

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'limite_hospedes', 'banheiros', 'animais', 'valor_limpeza', 'data_ativacao', 'data_criacao', 'data_atualizacao')

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'imovel', 'plataforma', 'taxa_plataforma', 'data_criacao', 'data_atualizacao')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'anuncio', 'checkin', 'checkout', 'preco_total', 'comentario', 'hospedes', 'data_criacao', 'data_atualizacao')