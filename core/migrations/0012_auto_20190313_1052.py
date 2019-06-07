# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-13 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190311_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(unique=True, upload_to='note/')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Page')),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='page',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='page',
        ),
    ]