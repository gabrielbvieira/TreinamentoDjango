from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Treinamento Django',
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    print(f'ID: {id}')
    produto = Produto.objects.get(id=id)
    context = {
        'produto': produto
    }
    return render(request, 'produto.html', context)