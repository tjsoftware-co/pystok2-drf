# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Program Category',
                'verbose_name_plural': 'Program Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgramChapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('priority', models.PositiveSmallIntegerField(default=0)),
                ('subtitle_1', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('subtext_1', models.CharField(max_length=1000, verbose_name='Subtext')),
                ('program', models.ForeignKey(to='eduprograms.Program')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgramFor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Program For',
                'verbose_name_plural': 'Programs For',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='program',
            name='program_category',
            field=models.ManyToManyField(to='eduprograms.ProgramCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='program',
            name='program_for',
            field=models.ManyToManyField(to='eduprograms.ProgramFor'),
            preserve_default=True,
        ),
    ]
