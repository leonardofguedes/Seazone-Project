from django.contrib import admin
from .models import Imovel


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = [
        'codigo_imovel', 'limite_hospedes', 'quantidade_banheiros', 'aceita_animais', 'valor_limpeza'
    ]