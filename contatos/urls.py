from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.HomeDetail.as_view(), name='home'),
    path('contato/<int:id>/', views.ContatoDetail.as_view(), name='contato'),
    path('novo_contato/', views.DashboardContatos.as_view(), name='novo_contato'),
    path('editar_contato_id/<int:id>/', views.DashboardContatos.as_view(), name='editar_contato_id'),
    path('deletar/<int:id>/', views.ContatoDelete.as_view(), name='deletar'),
]
