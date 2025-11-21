from django.shortcuts import render
from django.db.models import Q 
from django.shortcuts import get_object_or_404
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


def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    context = {
        'pessoa': pessoa
    }
    return render(request,'core/detalhe.html', context=context)
