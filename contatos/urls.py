from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('contato/<int:id>/', views.contato, name='contato'),
]
