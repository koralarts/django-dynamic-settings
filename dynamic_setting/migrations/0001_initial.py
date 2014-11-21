# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Setting Name', validators=[django.core.validators.RegexValidator('^[A-Z][A-Z0-9_]*[A-Z0-9]$', 'Enter a valid setting name. Example: SETTING_NAME_ITEM.')], unique=True)),
                ('data', models.TextField(default='-', verbose_name='Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
