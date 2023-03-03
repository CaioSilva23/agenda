from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.ContatosList.as_view(), name='home'),


    path('contato/<int:pk>/', views.ContatosDetail.as_view(), name='contato'),
    path('novo_contato/', views.ContatosList.as_view(), name='novo_contato'),
    path('deletar/<int:pk>/', views.ContatoDelete.as_view(), name='deletar'),

    path('editar_contato_id/<int:pk>/', views.ContatosDetail.as_view(), name='editar_contato_id'),
]
