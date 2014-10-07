# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=20, null=True, blank=True)),
                ('cnpj', models.CharField(max_length=20, null=True, blank=True)),
                ('data_cadastro', models.DateField()),
                ('endereco', models.CharField(max_length=100)),
                ('comp_endereco', models.CharField(max_length=100, null=True, blank=True)),
                ('cep', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=40)),
                ('telefone_1', models.CharField(max_length=12, null=True, blank=True)),
                ('telefone_2', models.CharField(max_length=12, null=True, blank=True)),
                ('celular', models.CharField(max_length=12, null=True, blank=True)),
                ('email', models.EmailField(max_length=50, null=True, blank=True)),
                ('nome_fantasia', models.CharField(max_length=100, null=True, blank=True)),
                ('data_admissao', models.DateField(null=True, blank=True)),
                ('cidade', models.ForeignKey(to='administrativo.Cidade')),
            ],
            options={
                'verbose_name': 'Pessoas',
                'verbose_name_plural': 'Pessoas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrecoProduto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_inicio_vigencia', models.DateField()),
                ('valor_vista', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor_prazo', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('data_cadastro', models.DateField()),
                ('producao_propria', models.BooleanField(default=0)),
                ('fora_linha', models.BooleanField(default=0)),
                ('categoria', models.ForeignKey(to='administrativo.CategoriaProduto')),
                ('cor', models.ForeignKey(to='administrativo.Cor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TamanhoProduto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tecido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.ForeignKey(to='administrativo.TamanhoProduto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='produto',
            name='tecido',
            field=models.ForeignKey(to='administrativo.Tecido', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade_medida',
            field=models.ForeignKey(to='administrativo.UnidadeMedida'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='precoproduto',
            name='produto',
            field=models.ForeignKey(to='administrativo.Produto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(to='administrativo.Estado'),
            preserve_default=True,
        ),
    ]
