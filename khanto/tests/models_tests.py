from django.test import TestCase
from khanto.models import Imovel, Anuncio, Reserva
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date, timedelta


class ImovelTestCase(TestCase):
    def setUp(self):
        Imovel.objects.create(limite_hospedes=2, banheiros=1, animais=True, valor_limpeza=100.0, data_ativacao='2022-01-01')

    def test_limite_hospedes(self):
        imovel = Imovel.objects.get(limite_hospedes=2)
        self.assertEqual(imovel.limite_hospedes, 2)

    def test_banheiros(self):
        imovel = Imovel.objects.get(banheiros=1)
        self.assertEqual(imovel.banheiros, 1)

    def test_animais(self):
        imovel = Imovel.objects.get(animais=True)
        self.assertTrue(imovel.animais)

    def test_valor_limpeza(self):
        imovel = Imovel.objects.get(valor_limpeza=100.0)
        self.assertEqual(imovel.valor_limpeza, 100.0)

    def test_data_ativacao(self):
        imovel = Imovel.objects.get(data_ativacao='2022-01-01')
        self.assertEqual(imovel.data_ativacao, '2022-01-01')


class AnuncioModelTest(TestCase):

    def setUp(self):
        self.imovel = Imovel.objects.create(
            nome='Casa Teste'
        )
        self.anuncio = Anuncio.objects.create(
            imovel=self.imovel,
            plataforma='Plataforma Teste',
            taxa_plataforma=10.0,
        )

    def test_anuncio_creation(self):
        self.assertTrue(isinstance(self.anuncio, Anuncio))
        self.assertEqual(self.anuncio.__str__(), 'Anuncio Casa Teste')

    def test_plataforma_validation(self):
        self.anuncio.plataforma = 'a' * 256
        self.assertRaises(ValidationError, self.anuncio.clean_fields)

    def test_imovel_relation(self):
        self.assertEqual(self.anuncio.imovel, self.imovel)

    def test_data_creation_and_update(self):
        self.assertIsNotNone(self.anuncio.data_criacao)
        self.assertIsNotNone(self.anuncio.data_atualizacao)


class ReservaModelTest(TestCase):

    def setUp(self):
        self.anuncio = Anuncio.objects.create(
            imovel=imovel,
            plataforma='Plataforma Teste',
            taxa_plataforma=10.0,
        )
        self.reserva = Reserva.objects.create(
            anuncio=self.anuncio,
            checkin=date.today(),
            checkout=date.today() + timedelta(days=5),
            preco_total=100.0,
            comentario='Comentário Teste',
            hospedes=2,
        )

    def test_reserva_creation(self):
        self.assertTrue(isinstance(self.reserva, Reserva))
        self.assertEqual(self.reserva.__str__(), 'Reserva ' + str(self.reserva.codigoReserva))

    def test_validations(self):
        self.reserva.checkin = date.today() + timedelta(days=10)
        self.reserva.checkout = date.today()
        self.assertRaises(ValidationError, self.reserva.clean_fields)
        self.reserva.hospedes = 0
        self.assertRaises(ValidationError, self.reserva.clean_fields)
        self.reserva.comentario = 'a'*256
        self.assertRaises(ValidationError, self.reserva.clean_fields)
    
    def test_anuncio_relation(self):
        self.assertEqual(self.reserva.anuncio, self.anuncio)
        
    def test_data_creation_and_update(self):
        self.assertIsNotNone(self.reserva.data_criacao)
        self.assertIsNotNone(self.reserva.data_atualizacao)

    def test_price_calculation(self):
        self.assertEqual(self.reserva.preco_total, 500.0)

