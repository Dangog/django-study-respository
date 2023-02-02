from django.urls import path

from recipes.views import contato, home, sobre, sugestoes

urlpatterns = [
    path('sobre/', sobre),
    path('', home),
    path('contato/', contato),
    path('sugestoes/', sugestoes)
]
