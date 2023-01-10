from django import forms
from khanto.models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['imovel', 'plataforma', 'taxa_plataforma']