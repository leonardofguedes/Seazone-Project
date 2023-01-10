from django.urls import path
from khanto.views.home_view import HomeView
from khanto.views.imoveis_views import ImovelList, ImovelDetail, ImovelUpdateView, ImovelCreateView, ImovelDeleteView, ImovelSearchView
from khanto.views.anuncio_view import AnuncioList, AnuncioUpdateView, AnuncioCreateView

urlpatterns = [
    path('imovel/', ImovelList.as_view(), name='imovel-list'),
    path('', HomeView.as_view(), name='home'),
    path('imovel/<int:pk>/', ImovelDetail.as_view(), name='imovel-detail'),
    path('imovel/edit/<int:pk>/', ImovelUpdateView.as_view(), name='imovel_update'),
    path('imovel/create/', ImovelCreateView.as_view(), name='imovel_create'),
    path('imovel/delete/<int:pk>/', ImovelDeleteView.as_view(), name='imovel-delete'),
    path('imovel/search/', ImovelSearchView.as_view(), name='imovel-search'),
    #anuncio
    path('anuncio/', AnuncioList.as_view(), name='anuncio-list'),
    path('anuncio/edit/<int:pk>/', AnuncioUpdateView.as_view(), name='anuncio_update'),
    path('anuncio/create/', AnuncioCreateView.as_view(), name='anuncio_create'),
]
