# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentItemSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocol', models.CharField(max_length=32, verbose_name=b'protocol')),
                ('remote_host', models.IPAddressField(verbose_name=b'remote host')),
                ('remote_port', models.IntegerField(verbose_name=b'remote port')),
                ('local_host', models.IPAddressField(verbose_name=b'local host')),
                ('local_port', models.IntegerField(verbose_name=b'local port')),
                ('count', models.IntegerField(verbose_name=b'count')),
                ('generator', models.BooleanField(default=False, verbose_name=b'defines whether item set is generated or not')),
                ('jep', models.BooleanField(default=False, db_column=b'ejp')),
                ('interesting', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'freq_itemsets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name=b'operation start time', db_column=b'start_time')),
                ('end', models.DateTimeField(verbose_name=b'operation end time', db_column=b'end_time')),
                ('minimal_sup', models.SmallIntegerField(verbose_name=b'not used', db_column=b'minsup')),
                ('interval', models.IntegerField(verbose_name=b'time interval in seconds', db_column=b'interval')),
                ('request_id', models.IntegerField(verbose_name=b'not used')),
                ('tag', models.CharField(max_length=32, verbose_name=b'operation tag')),
            ],
            options={
                'db_table': 'operations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='frequentitemset',
            name='operation',
            field=models.ForeignKey(db_column=b'oid', verbose_name=b'operation', to='miner.Operation'),
            preserve_default=True,
        ),
    ]
