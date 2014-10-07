# -*- coding: utf-8 -*-
from django.db import models
import administrativo
import financeiro

class NaturezaOperacao(models.Model):
    codigo_natureza = models.IntegerField()
    descricao = models.CharField(max_length=100)
    descricao_reduzida = models.CharField(max_length=40)
    ativo = models.BooleanField(default=1)
	
    class Meta:
        verbose_name = "Natureza de Operação"
        verbose_name_plural = "Naturezas de Operação"

class TipoMovimento(models.Model):
    descricao = models.CharField(max_length=40)
    contabiliza = models.BooleanField(default=0)
    gera_contas_a_pagar = models.BooleanField(default=0)
    gera_estoque = models.BooleanField(default=0)
    tipo_documento = models.ForeignKey('financeiro.TipoDocumento', null=True)
	
    class Meta:
        verbose_name = "Tipo de Movimento"
        verbose_name_plural = "Tipos de Movimento"
	
class NotaFiscal(models.Model):
    numero_nota_fiscal = models.IntegerField()
    serie = models.CharField(max_length=3)
    natureza_operacao = models.ForeignKey('compra.NaturezaOperacao')
    tipo_movimento = models.ForeignKey('compra.TipoMovimento')
    pessoa = models.ForeignKey('administrativo.Pessoa')
    data_emissao = models.DateField()
    data_lancamento = models.DateField()
    valor_mercadoria = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total_nota = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(max_length=100, blank=True, null=True)
    chave_acesso_nfe = models.CharField(max_length=40, blank=True, null=True)
	
    class Meta:
        verbose_name = "Nota Fiscal"
        verbose_name_plural = "Notas Fiscais"
	
class ImpostosNotaFiscal(models.Model):
    nota_fiscal = models.OneToOneField('compra.NotaFiscal')
    valor_base_icms = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_icms = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_base_substituicao = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_substituicao = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_base_ipi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_ipi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_frete = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_seguro = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_descontos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_outras_despesas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_pis = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_cofins = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	
    class Meta:
        verbose_name = "Impostos de Nota Fiscal"
        verbose_name_plural = "Impostos de Nota Fiscal"

class ItemNotaFiscal(models.Model):
    nota_fiscal = models.ForeignKey('compra.NotaFiscal')
    produto = models.ForeignKey('administrativo.Produto')
    natureza_operacao = models.ForeignKey('compra.NaturezaOperacao')
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantidade = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    valor_total_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	
    class Meta:
        verbose_name = "Item de Nota Fiscal"
        verbose_name_plural = "Itens de Nota Fiscal"