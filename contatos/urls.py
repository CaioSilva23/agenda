from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', lambda request: redirect('/contatos/home/', request)),
    path('home/', views.home, name='home'),
    path('contato/<int:id>/', views.contato, name='contato'),

    path('novo_contato/', views.novo_contato, name='novo_contato'),
    path('editar_contato_id/<int:id>/', views.editar_contato_id, name='editar_contato_id'),
]
