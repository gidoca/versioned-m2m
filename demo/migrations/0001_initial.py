# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versions.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstModel',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('identity', models.CharField(max_length=36)),
                ('version_start_date', models.DateTimeField()),
                ('version_end_date', models.DateTimeField(default=None, null=True, blank=True)),
                ('version_birth_date', models.DateTimeField()),
                ('f', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Intermediary',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('identity', models.CharField(max_length=36)),
                ('version_start_date', models.DateTimeField()),
                ('version_end_date', models.DateTimeField(default=None, null=True, blank=True)),
                ('version_birth_date', models.DateTimeField()),
                ('firstmodel', models.ForeignKey(to='demo.FirstModel')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecondModel',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('identity', models.CharField(max_length=36)),
                ('version_start_date', models.DateTimeField()),
                ('version_end_date', models.DateTimeField(default=None, null=True, blank=True)),
                ('version_birth_date', models.DateTimeField()),
                ('g', models.TextField()),
                ('other', versions.models.VersionedManyToManyField(to='demo.FirstModel', through='demo.Intermediary')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='secondmodel',
            unique_together=set([('id', 'identity')]),
        ),
        migrations.AddField(
            model_name='intermediary',
            name='secondmodel',
            field=models.ForeignKey(to='demo.SecondModel'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='intermediary',
            unique_together=set([('id', 'identity')]),
        ),
        migrations.AlterUniqueTogether(
            name='firstmodel',
            unique_together=set([('id', 'identity')]),
        ),
    ]
