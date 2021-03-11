from django.contrib import admin

from .models import Agenda


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email', 'endereco', 'bairro', 'cep', 'cidade', 'data_add', 'usuario')
    list_display_links = ('id', 'nome', 'telefone')
    search_fields = 'nome',
    list_filter = ('nome', 'telefone')
    list_per_page = 10

admin.site.register(Agenda, AgendaAdmin)
