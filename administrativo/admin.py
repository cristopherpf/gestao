# -*- coding: utf-8 -*-
from django.contrib import admin
from administrativo.models import *

class PessoaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações', {'fields': ['nome', 'cpf', 'cnpj', 'data_cadastro', 'telefone_1', 'telefone_2', 'email']}),
        ('Endereço', {'fields': ['cidade', 'endereco', 'comp_endereco', 'bairro', 'cep']}),
		('Dados Cliente', {'fields': ['nome_fantasia'], 'classes': ['collapse']}),
		('Dados Fornecedor', {'fields': ['nome_fantasia'], 'classes': ['collapse']}),
		('Dados Funcionário', {'fields': ['data_admissao'], 'classes': ['collapse']}),
    ]
    list_display = ('nome', 'cidade', 'telefone_1', 'email')
    list_filter = ['data_cadastro', 'cidade']
    search_fields = ['nome', 'telefone_1', 'email']

admin.site.register(Pessoa, PessoaAdmin)
	
class PrecoProdutoInline(admin.TabularInline):
    model = PrecoProduto
    extra = 0
    #fields = ('nr_parcela', 'data_vencimento', 'data_vencto_ajustada', 'valor_parcela', 'valor_saldo', 'situacao')
    #readonly_fields = ['nr_parcela', 'situacao', 'valor_saldo']
	
class ProdutoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações', {'fields': ['descricao', 'categoria', 'unidade_medida', 'data_cadastro', 'producao_propria', 'fora_linha']}),
		('Informações Uniforme', {'fields': ['cor', 'tamanho', 'tecido']}),
    ]
    list_display = ('descricao', 'categoria', 'unidade_medida')
    list_filter = ['categoria']
    search_fields = ['descricao']
    inlines = [PrecoProdutoInline]

admin.site.register(Produto, ProdutoAdmin)
	
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    #def save_model(self, request, obj, form, change):
        #obj.nr_parcela = 1
        #obj.save()
		
admin.site.register(Estado, EstadoAdmin)

######################
admin.site.register(Cidade)
admin.site.register(Cor)
admin.site.register(Tecido)
admin.site.register(UnidadeMedida)
admin.site.register(TamanhoProduto)
admin.site.register(CategoriaProduto)
