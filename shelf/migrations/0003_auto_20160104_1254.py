# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20151207_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('isbn', models.CharField(max_length=17)),
                ('date', models.DateField()),
                ('book', models.ForeignKey(to='shelf.Book')),
                ('publisher', models.ForeignKey(to='shelf.Publisher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('catalogue_number', models.CharField(max_length=30)),
                ('cover_type', models.CharField(max_length=4, choices=[('soft', 'soft'), ('hard', 'hard')])),
                ('edition', models.ForeignKey(to='shelf.BookEdition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='shelf.Author'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='shelf.BookCategory'),
            preserve_default=True,
        ),
    ]
