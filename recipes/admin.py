from django.contrib import admin

from recipes.models import Categoria, Receita

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...
