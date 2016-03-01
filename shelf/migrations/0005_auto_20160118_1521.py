# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20160106_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(related_name='editions', to='shelf.Book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(blank=True, max_length=17),
            preserve_default=True,
        ),
    ]
