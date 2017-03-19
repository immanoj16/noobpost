# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-19 06:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 3, 18, 23, 50, 59, 892000))),
                ('similar', models.ManyToManyField(blank=True, null=True, related_name='_tutorial_similar_+', to='tutorial.Tutorial')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('youtube_id', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 3, 18, 23, 50, 59, 891000))),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='videos',
            field=models.ManyToManyField(to='tutorial.Video'),
        ),
    ]
