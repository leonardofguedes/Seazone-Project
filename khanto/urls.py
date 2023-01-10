from django.urls import path
from khanto.views.home_view import HomeView
from khanto.views.imoveis_views import ImovelList, ImovelDetail, ImovelUpdateView, ImovelCreateView, ImovelDeleteView
from khanto.views.anuncio_view import AnuncioList, AnuncioUpdateView, AnuncioCreateView
from khanto.views.reservas_view import ReservaList, ReservaCreateView, ReservaDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #imovel
    path('imovel/', ImovelList.as_view(), name='imovel-list'),
    path('imovel/<int:pk>/', ImovelDetail.as_view(), name='imovel-detail'),
    path('imovel/edit/<int:codigoImovel>/', ImovelUpdateView.as_view(), name='imovel_update'),
    path('imovel/create/', ImovelCreateView.as_view(), name='imovel_create'),
    path('imovel/delete/<int:pk>/', ImovelDeleteView.as_view(), name='imovel-delete'),
    #path('imovel/search/', ImovelSearchView.as_view(), name='imovel-search'),
    #anuncio
    path('anuncio/', AnuncioList.as_view(), name='anuncio-list'),
    path('anuncio/edit/<int:pk>/', AnuncioUpdateView.as_view(), name='anuncio_update'),
    path('anuncio/create/', AnuncioCreateView.as_view(), name='anuncio_create'),
    #path('anuncio/search/', AnuncioSearchView.as_view(), name='anuncio-search'),
    #reservas
    path('reserva/', ReservaList.as_view(), name='reserva-list'),
    path('reserva/create/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva-delete'),
]
