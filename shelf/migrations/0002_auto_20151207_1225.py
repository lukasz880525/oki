# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=17)),
                ('author', models.ForeignKey(to='shelf.Author')),
                ('publisher', models.ForeignKey(to='shelf.Publisher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bookedition',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bookedition',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='BookEdition',
        ),
    ]
