# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, verbose_name='\u8bfe\u7a0b\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('creadit', models.IntegerField(verbose_name='\u5b66\u5206')),
            ],
            options={
                'db_table': 'course',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sec_id', models.CharField(max_length=10, verbose_name='\u5b66\u671f\u7f16\u53f7')),
                ('desc', models.TextField(verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('start_week', models.IntegerField(verbose_name='\u8d77\u59cb\u5468')),
                ('end_week', models.IntegerField(verbose_name='\u7ed3\u675f\u5468')),
                ('day', models.IntegerField(verbose_name='\u5468\u51e0')),
                ('start_time', models.IntegerField(verbose_name='\u4e0a\u8bfe\u65f6\u95f4')),
                ('end_time', models.IntegerField(verbose_name='\u4e0b\u8bfe\u65f6\u95f4')),
                ('MAX_NUM', models.IntegerField(verbose_name='\u4eba\u6570')),
                ('year', models.IntegerField(verbose_name='\u5b66\u5e74')),
                ('building', models.ForeignKey(to='organization.ClassRoom')),
                ('course_id', models.ForeignKey(to='course.Course')),
                ('teachers', models.ForeignKey(to='teacher.Teacher')),
            ],
            options={
                'db_table': 'section',
                'verbose_name_plural': '\u5f00\u8bfe',
            },
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(verbose_name='\u5206\u6570')),
                ('s_id', models.ForeignKey(to='student.Student')),
                ('sec_id', models.ForeignKey(to='course.Section')),
            ],
            options={
                'db_table': 'take',
                'verbose_name_plural': '\u9009\u8bfe',
            },
        ),
    ]
