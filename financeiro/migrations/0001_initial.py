# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTituloPagar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_parcela', models.IntegerField()),
                ('data_vencimento', models.DateField()),
                ('data_vencto_ajustada', models.DateField(null=True, blank=True)),
                ('valor_parcela', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor_saldo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('situacao', models.CharField(default=b'AB', max_length=2, choices=[(b'AB', b'Aberto'), (b'PG', b'Pago'), (b'CA', b'Cancelado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemTituloReceber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_parcela', models.IntegerField()),
                ('data_vencimento', models.DateField()),
                ('data_vencto_ajustada', models.DateField(null=True, blank=True)),
                ('valor_parcela', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor_saldo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('situacao', models.CharField(default=b'AB', max_length=2, choices=[(b'AB', b'Aberto'), (b'PG', b'Pago'), (b'CA', b'Cancelado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TituloPagar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_documento', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=40)),
                ('data_entrada', models.DateField()),
                ('valor_titulo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('observacao', models.TextField(max_length=100, null=True, blank=True)),
                ('pessoa', models.ForeignKey(to='administrativo.Pessoa')),
                ('tipo_documento', models.ForeignKey(to='financeiro.TipoDocumento')),
            ],
            options={
                'verbose_name': 'T\xedtulo a Pagar',
                'verbose_name_plural': 'T\xedtulos a Pagar',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TituloReceber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_documento', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=40)),
                ('data_entrada', models.DateField()),
                ('valor_titulo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('observacao', models.TextField(max_length=100, null=True, blank=True)),
                ('pessoa', models.ForeignKey(to='administrativo.Pessoa')),
                ('tipo_documento', models.ForeignKey(to='financeiro.TipoDocumento')),
            ],
            options={
                'verbose_name': 'T\xedtulo a Receber',
                'verbose_name_plural': 'T\xedtulos a Receber',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='itemtituloreceber',
            name='titulo_receber',
            field=models.ForeignKey(to='financeiro.TituloReceber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemtitulopagar',
            name='titulo_pagar',
            field=models.ForeignKey(to='financeiro.TituloPagar'),
            preserve_default=True,
        ),
    ]
