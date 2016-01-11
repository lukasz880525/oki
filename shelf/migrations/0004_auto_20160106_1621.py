# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20160104_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='first_name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last_name'),
            preserve_default=True,
        ),
    ]
