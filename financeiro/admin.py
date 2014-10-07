# -*- coding: utf-8 -*-
from django.contrib import admin
from financeiro.models import *
	
class ItemTituloPagarInline(admin.TabularInline):
    model = ItemTituloPagar
    extra = 0
    fields = ('nr_parcela', 'data_vencimento', 'data_vencto_ajustada', 'valor_parcela', 'valor_saldo', 'situacao')
    readonly_fields = ['nr_parcela', 'situacao', 'valor_saldo']
	
class TituloPagarAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'numero_documento', 'tipo_documento', 'pessoa', 'data_entrada', 'valor_titulo')
    list_filter = ['tipo_documento', 'pessoa', 'data_entrada']
    search_fields = ['descricao', 'numero_documento']
    inlines = [ItemTituloPagarInline]
	
    def save_formset(self, request, form, formset, change):
        #if formset.model != ItemTituloPagarInline:
        #    return super(TituloPagarAdmin, self).save_formset(request, form, formset, change)
        instances = formset.save(commit=False)
        for instance in instances:
            print change
            if change == False:
                parcelas = ItemTituloPagar.objects.filter(titulo_pagar = instance.titulo_pagar)
                print parcelas.count()
                instance.nr_parcela = parcelas.count() + 1
                instance.valor_saldo = instance.valor_parcela
                instance.save()
        formset.save_m2m()

admin.site.register(TituloPagar, TituloPagarAdmin)
		
class ItemTituloReceberInline(admin.TabularInline):
    model = ItemTituloReceber
    extra = 0
    fields = ('nr_parcela', 'data_vencimento', 'data_vencto_ajustada', 'valor_parcela', 'valor_saldo', 'situacao')
    readonly_fields = ['nr_parcela', 'situacao', 'valor_saldo']
	
class TituloReceberAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'numero_documento', 'tipo_documento', 'pessoa', 'data_entrada', 'valor_titulo')
    list_filter = ['tipo_documento', 'pessoa', 'data_entrada']
    search_fields = ['descricao', 'numero_documento']
    inlines = [ItemTituloReceberInline]
	
admin.site.register(TituloReceber, TituloReceberAdmin)	
	
class ItemTituloPagarAdmin(admin.ModelAdmin):
    list_display = ('get_titulo_pagar_desc', 'nr_parcela', 'data_vencimento', 'data_vencto_ajustada', 'valor_parcela', 'valor_saldo')
    list_filter = ['data_vencimento', 'situacao']
    #search_fields = ['numero_documento']
    #inlines = [ItemTituloPagarInline]

admin.site.register(ItemTituloPagar, ItemTituloPagarAdmin)
################################
admin.site.register(TipoDocumento)
