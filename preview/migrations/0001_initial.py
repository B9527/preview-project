# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 06:44
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.TextField()),
                ('database', models.TextField()),
                ('schema', models.TextField(blank=True, null=True)),
                ('username', models.TextField()),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'mdatabase',
            },
        ),
        migrations.CreateModel(
            name='PreviewConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.TextField()),
                ('database', models.TextField()),
                ('schema', models.TextField(blank=True, null=True)),
                ('table', models.TextField()),
                ('status', models.TextField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'preview_config',
            },
        ),
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.TextField()),
                ('field', models.TextField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preview.Database')),
            ],
            options={
                'db_table': 'table_data',
            },
        ),
    ]
