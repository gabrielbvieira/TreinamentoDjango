from django.shortcuts import render

def index(request):
    if str(request.user) == 'AnnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'
    
    context = {
        'curso': 'Treinamento Django',
        'logado': teste
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')