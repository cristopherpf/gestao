# -*- coding: utf-8 -*-
from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
	
    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    estado = models.ForeignKey('administrativo.Estado')
    nome = models.CharField(max_length=100)
	
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True) 
    data_cadastro = models.DateField()
    cidade = models.ForeignKey('administrativo.Cidade')
    endereco = models.CharField(max_length=100)
    comp_endereco = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=100)
    bairro = models.CharField(max_length=40)
    telefone_1 = models.CharField(max_length=12, blank=True, null=True)
    telefone_2 = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    data_admissao = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Pessoas"
        verbose_name_plural = "Pessoas"
	
    def __str__(self):
        return self.nome
		
class CategoriaProduto(models.Model):
    descricao = models.CharField(max_length=40)
	
    def __str__(self):
        return self.descricao
		
class Cor(models.Model):
    nome = models.CharField(max_length=40)
	
    def __str__(self):
        return self.nome
		
class Tecido(models.Model):
    descricao = models.CharField(max_length=40)
	
    def __str__(self):
        return self.descricao
		
class TamanhoProduto(models.Model):
    descricao = models.CharField(max_length=40)
    sigla = models.CharField(max_length=2)
	
    def __str__(self):
        return self.descricao
		
class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=40)
    sigla = models.CharField(max_length=2)
	
    def __str__(self):
        return self.descricao
		
class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey('administrativo.CategoriaProduto')
    unidade_medida = models.ForeignKey('administrativo.UnidadeMedida')
    cor = models.ForeignKey('administrativo.Cor', null=True)
    tamanho = models.ForeignKey('administrativo.TamanhoProduto', null=True)
    tecido = models.ForeignKey('administrativo.Tecido', null=True)
    data_cadastro = models.DateField()
    producao_propria = models.BooleanField(default=0)
    fora_linha = models.BooleanField(default=0)
	
    def __str__(self):
        return self.descricao
		
class PrecoProduto(models.Model):
    produto = models.ForeignKey('administrativo.Produto')
    data_inicio_vigencia = models.DateField()
    valor_vista = models.DecimalField(max_digits=10, decimal_places=2)
    valor_prazo = models.DecimalField(max_digits=10, decimal_places=2)