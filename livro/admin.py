from django.contrib import admin
from .models import Livros, Categoria, Emprestimos


class LivrosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'autor']

admin.site.register(Livros, LivrosAdmin)

admin.site.register(Categoria)
admin.site.register(Emprestimos)