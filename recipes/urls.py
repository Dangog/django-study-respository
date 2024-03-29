from django.urls import path

from . import views

# Nome do app:
app_name = "recipes"

urlpatterns = [
    path('', views.home, name="inicial"),
    path('recipe/<int:id>/', views.recipe, name="receita"),
    path('recipe/categoria/<int:categoria_id>/', views.categoria, name="categoria")
]
