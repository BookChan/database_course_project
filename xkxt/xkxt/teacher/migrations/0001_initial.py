# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, verbose_name='\u6559\u5e08\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(max_length=1, verbose_name='\u6027\u522b', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('dep_id', models.ForeignKey(to='organization.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'teacher',
                'verbose_name_plural': '\u6559\u5e08',
            },
        ),
    ]
