# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'report creation date')),
                ('start_time', models.DateTimeField(verbose_name=b'Upper time bracket')),
                ('end_time', models.DateTimeField(verbose_name=b'Lower time bracket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('one_hour_occurrences', models.IntegerField(verbose_name=b'one hour window occurrences')),
                ('two_hour_occurrences', models.IntegerField(verbose_name=b'two hours window occurrences')),
                ('four_hour_occurrences', models.IntegerField(verbose_name=b'four hours window occurrences')),
                ('eight_hour_occurrences', models.IntegerField(verbose_name=b'eight hours window occurrences')),
                ('sixteen_hour_occurrences', models.IntegerField(verbose_name=b'sixteen hours window occurrences')),
                ('total_occurrences', models.IntegerField(verbose_name=b'total previous occurrences')),
                ('frequent_item_set', models.ForeignKey(verbose_name=b'frequent item sets', to='miner.FrequentItemSet', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='items',
            field=models.ManyToManyField(to='reports.ReportItem', verbose_name=b'report items'),
            preserve_default=True,
        ),
    ]
