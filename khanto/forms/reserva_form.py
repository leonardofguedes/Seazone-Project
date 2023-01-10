from django import forms
from khanto.models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['anuncio', 'checkin', 'checkout', 'preco_total', 'comentario', 'hospedes']
