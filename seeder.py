import random
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        from khanto.models import Imovel

        codigos_imoveis = [
            'ABC123', 'DEF456', 'GHI789', 'JKL012', 'MNO345', 'PQR678'
        ]
        limites_hospedes = [2, 4, 6, 8, 10]
        quantidades_banheiros = [1, 2]
        valores_limpeza = [50, 100, 150, 200]
        data_ativacao = '2022-01-01'
        
        for codigo_imovel in codigos_imoveis:
            imovel = Imovel(
                codigo_imovel=codigo_imovel,
                limite_hospedes=random.choice(limites_hospedes),
                quantidade_banheiros=random.choice(quantidades_banheiros),
                aceita_animais=random.choice([True, False]),
                valor_limpeza=random.choice(valores_limpeza),
                data_ativacao=data_ativacao
            )
            imovel.save()
        self.stdout.write(self.style.SUCCESS('Unidades de imóveis criadas com sucesso'))

