from django.shortcuts import render
from django.db.models import Q 
from . models import Pessoa

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def lista(request):
    pesquisa = request.GET.get('pesquisa', '')
    # pessoas = Pessoa.objects.filter(biografia__contains=pesquisa)
    pessoas = Pessoa.objects.filter(
        Q(nome__icontains=pesquisa) |
        Q(biografia__icontains=pesquisa)
        )

    context = {
        'pessoas': pessoas
    }
    return render(request, 'core/lista.html', context=context)
