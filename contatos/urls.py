from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.ContatosList.as_view(), name='home'),
    path('filtro_contatos/', views.FiltroContatosList.as_view(), name='filtro_contatos'),
    path('novo_contato/', views.ContatosList.as_view(), name='novo_contato'),


    path('contato/<int:pk>/', views.ContatoDetalhes.as_view(), name='contato'),
    path('deletar/<int:pk>/', views.ContatoDeleteView.as_view(), name='deletar'),

    path('editar_contato_id/<int:pk>/', views.ContatoDetalhes.as_view(), name='editar_contato_id'),

    path('nova_categoria/', views.PostCategoria.as_view(), name='nova_categoria')
]
