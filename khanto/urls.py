from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImovelList.as_view(), name='imovel-list'),
    path('<int:pk>/', views.ImovelDetail.as_view(), name='imovel-detail'),
    path('edit/<int:pk>/', views.ImovelUpdateView.as_view(), name='imovel_update'),
    path('create/', views.ImovelCreateView.as_view(), name='imovel_create'),
    path('delete/<int:pk>/', views.ImovelDeleteView.as_view(), name='imovel-delete'),
    path('search/', views.ImovelSearchView.as_view(), name='imovel-search'),

]