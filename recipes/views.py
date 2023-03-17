from django.http import Http404
from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Receita


# Create your views here.
def home(request):
    receitas = Receita.objects.filter(
        estaPublicado=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': receitas,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'pagina_de_detalhes': True,
    })


def categoria(request, categoria_id):
    receitas = Receita.objects.filter(
        categoria__id=categoria_id,
        estaPublicado=True
    ).order_by('-id')

    if not receitas:
        raise Http404("Página não encontrada! Tente novamente")

    return render(request, 'recipes/pages/category.html', context={
        'recipes': receitas,
        'titulo':  f'{receitas.last().categoria.nome} - Categoria',
    })
