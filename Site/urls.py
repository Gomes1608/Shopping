from django.urls import path
from Site import views

urlpatterns = [
    path("", views.index, name="index"),
    path('sobre-a-empresa' , views.institucional, name= 'institucional'),
    path("Cadastro", views.Cadastro, name="Cadastro"),
    path("Contato", views.Contato, name="Contato"),
    path("produtos", views.produto_lista, name="produto lista"),
    path("produto", views.produto_detalhe, name="produto_detalhe"),
]