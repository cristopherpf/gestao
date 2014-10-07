# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpostosNotaFiscal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_base_icms', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_icms', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_base_substituicao', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_substituicao', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_base_ipi', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_ipi', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_frete', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_seguro', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_descontos', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_outras_despesas', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_pis', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valor_cofins', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemNotaFiscal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_unitario', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('quantidade', models.DecimalField(default=0, max_digits=12, decimal_places=4)),
                ('valor_total_item', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NaturezaOperacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_natureza', models.IntegerField()),
                ('descricao', models.CharField(max_length=100)),
                ('descricao_reduzida', models.CharField(max_length=40)),
                ('ativo', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_nota_fiscal', models.IntegerField()),
                ('serie', models.CharField(max_length=3)),
                ('data_emissao', models.DateField()),
                ('data_lancamento', models.DateField()),
                ('valor_mercadoria', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor_total_nota', models.DecimalField(max_digits=10, decimal_places=2)),
                ('observacao', models.TextField(max_length=100, null=True, blank=True)),
                ('chave_acesso_nfe', models.CharField(max_length=40, null=True, blank=True)),
                ('natureza_operacao', models.ForeignKey(to='compra.NaturezaOperacao')),
                ('pessoa', models.ForeignKey(to='administrativo.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoMovimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('contabiliza', models.BooleanField(default=0)),
                ('gera_contas_a_pagar', models.BooleanField(default=0)),
                ('gera_estoque', models.BooleanField(default=0)),
                ('tipo_documento', models.ForeignKey(to='financeiro.TipoDocumento', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notafiscal',
            name='tipo_movimento',
            field=models.ForeignKey(to='compra.TipoMovimento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemnotafiscal',
            name='natureza_operacao',
            field=models.ForeignKey(to='compra.NaturezaOperacao'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemnotafiscal',
            name='nota_fiscal',
            field=models.ForeignKey(to='compra.NotaFiscal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemnotafiscal',
            name='produto',
            field=models.ForeignKey(to='administrativo.Produto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='impostosnotafiscal',
            name='nota_fiscal',
            field=models.OneToOneField(to='compra.NotaFiscal'),
            preserve_default=True,
        ),
    ]
