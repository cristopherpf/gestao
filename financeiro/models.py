# -*- coding: utf-8 -*-
from django.db import models
import administrativo

# Create your models here.		
class TipoDocumento(models.Model):
    descricao = models.CharField(max_length=100)
	
    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"
	
    def __str__(self):
        return self.descricao

class TituloPagar(models.Model):
    numero_documento = models.CharField(max_length=20)
    descricao = models.CharField(max_length=40)
    tipo_documento = models.ForeignKey('financeiro.TipoDocumento')
    pessoa = models.ForeignKey('administrativo.Pessoa')
    data_entrada = models.DateField()
    valor_titulo = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(max_length=100, blank=True, null=True)
	
    class Meta:
        verbose_name = "Título a Pagar"
        verbose_name_plural = "Títulos a Pagar"

class ItemTituloPagar(models.Model):
    SITUACAO_TITULO = (
        ('AB', 'Aberto'),
        ('PG', 'Pago'),
        ('CA', 'Cancelado'),
    )
    titulo_pagar = models.ForeignKey('financeiro.TituloPagar')
    nr_parcela = models.IntegerField()
    data_vencimento = models.DateField()
    data_vencto_ajustada = models.DateField(blank=True, null=True)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    valor_saldo = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=2, choices=SITUACAO_TITULO, default='AB')
	
    def get_titulo_pagar_desc(self):
        return self.titulo_pagar.descricao;
    get_titulo_pagar_desc.short_description = 'Descrição'
	
class TituloReceber(models.Model):
    numero_documento = models.CharField(max_length=20)
    descricao = models.CharField(max_length=40)
    tipo_documento = models.ForeignKey('financeiro.TipoDocumento')
    pessoa = models.ForeignKey('administrativo.Pessoa')
    data_entrada = models.DateField()
    valor_titulo = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(max_length=100, blank=True, null=True)
	
    class Meta:
        verbose_name = "Título a Receber"
        verbose_name_plural = "Títulos a Receber"

class ItemTituloReceber(models.Model):
    SITUACAO_TITULO = (
        ('AB', 'Aberto'),
        ('PG', 'Pago'),
        ('CA', 'Cancelado'),
    )
    titulo_receber = models.ForeignKey('financeiro.TituloReceber')
    nr_parcela = models.IntegerField()
    data_vencimento = models.DateField()
    data_vencto_ajustada = models.DateField(blank=True, null=True)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    valor_saldo = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=2, choices=SITUACAO_TITULO, default='AB')
	
    def get_titulo_receber_desc(self):
        return self.titulo_receber.descricao;
    get_titulo_receber_desc.short_description = 'Descrição'