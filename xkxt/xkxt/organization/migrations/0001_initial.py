# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.CharField(max_length=10, verbose_name='\u697c\u540d')),
                ('room_id', models.CharField(max_length=10, verbose_name='\u623f\u95f4\u7f16\u53f7')),
                ('capicity', models.IntegerField(verbose_name='\u5ea7\u4f4d\u6570')),
            ],
            options={
                'db_table': 'classroom',
                'verbose_name': '\u6559\u5ba4',
                'verbose_name_plural': '\u6559\u5ba4',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, verbose_name='\u9662\u7cfb\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u9662\u7cfb\u540d\u79f0')),
            ],
            options={
                'db_table': 'department',
                'verbose_name_plural': '\u9662\u7cfb',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, verbose_name='\u4e13\u4e1a\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u4e13\u4e1a\u540d\u79f0')),
                ('dep_id', models.ForeignKey(verbose_name=b'\xe9\x99\xa2\xe7\xb3\xbb', to='organization.Department')),
            ],
            options={
                'db_table': 'major',
                'verbose_name_plural': '\u4e13\u4e1a',
            },
        ),
    ]
