from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, "index.html")

def produto_lista(request):
    return render(request, "produtos.html")

def produto_detalhe(request):
    return render(request, "produto_detalhes.html")
def institucional(request):
    return render(request, "empresa.html")
def Contato(request):
    return render(request, "Contato.html")
def Cadastro(request):
    return render(request, "Cadastro.html")