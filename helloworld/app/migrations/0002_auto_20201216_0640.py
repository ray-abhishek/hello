# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email', blank=True)),
                ('phone', models.CharField(max_length=20, verbose_name=b'Phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Myfile',
        ),
    ]
