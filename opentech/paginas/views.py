from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cliente(request):
    return render(request, 'cliente.html')

def localizacao(request):
    return render(request, 'localizacao.html')

def servicos(request):
    return render(request, 'servicos.html')

def sobre(request):
    return render(request, 'sobre.html')

def vagas(request):
    return render(request, 'vagas.html')


