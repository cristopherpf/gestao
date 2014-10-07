# -*- coding: utf-8 -*-
from django.contrib import admin
from compra.models import *

class ImpostosNotaFiscalInline(admin.StackedInline):
    model = ImpostosNotaFiscal
	
class ItensNotaFiscalInline(admin.TabularInline):
    model = ItemNotaFiscal
    extra = 0
	
class NotaFiscalAdmin(admin.ModelAdmin):
    inlines = [ImpostosNotaFiscalInline, ItensNotaFiscalInline]

admin.site.register(NotaFiscal, NotaFiscalAdmin)

##########################################	
admin.site.register(NaturezaOperacao)
admin.site.register(TipoMovimento)
