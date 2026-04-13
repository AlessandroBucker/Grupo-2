#Criando a url (rota) para a view de listar as empresas

from django.urls import path
from .views import listar_empresas

urlpatterns = [
    path('empresas/', listar_empresas),
]