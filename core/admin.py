
from django.contrib import admin
from django.utils.html import format_html
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'foto_preview', 'data_criacao', 'data_modificacao')
    list_display_links = ('data_criacao',)
    list_editable = ('nome',)
    search_fields = ('nome', 'biografia')
    list_filter = ('data_criacao', 'data_modificacao')
    ordering = ('-data_criacao',)
    readonly_fields = ('data_criacao', 'data_modificacao', 'foto_preview')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'biografia', 'url_foto', 'foto_preview')
        }),
        ('Controle de Datas', {
            'fields': ('data_criacao', 'data_modificacao')
        }),
    )

    # Método para mostrar a foto no admin
    def foto_preview(self, obj):
        if obj.url_foto:
            return format_html('<img src="{}" width="100" style="object-fit: cover;"/>', obj.url_foto)
        return "-"
    foto_preview.short_description = 'Foto'




'''

from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista do admin
    list_display = ('nome', 'data_criacao', 'data_modificacao')
    
    # Define qual coluna será o link para o formulário de edição
    list_display_links = ('data_criacao',)  # agora o link é a data_criacao
    
    # Campos que podem ser editados diretamente na lista
    list_editable = ('nome',)  # nome é editável sem abrir o detalhe
    
    # Campos que podem ser pesquisados
    search_fields = ('nome', 'biografia')
    
    # Filtros laterais
    list_filter = ('data_criacao', 'data_modificacao')
    
    # Ordenação padrão da lista (mais recente primeiro)
    ordering = ('-data_criacao',)
    
    # Campos que ficam somente leitura no admin
    readonly_fields = ('data_criacao', 'data_modificacao')
    
    # Campos do formulário no admin (ordem e agrupamento)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'biografia', 'url_foto')
        }),
        ('Controle de Datas', {
            'fields': ('data_criacao', 'data_modificacao')
        }),
    )

'''
