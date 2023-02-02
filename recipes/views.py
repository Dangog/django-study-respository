from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'global/home.html')


def sobre(request):

    return HttpResponse("Você se encontra na página: sobre!")
    # Return HTTP response


def contato(request):
    return render(request, 'recipes/contato.html')


def sugestoes(request):
    return render(request, 'recipes/sugestoes.html')
