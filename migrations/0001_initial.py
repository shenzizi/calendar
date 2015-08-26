# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'defaultvalue', max_length=50)),
                ('phone', models.CharField(default=b'defaultvalue', max_length=10)),
                ('submittedtime', models.DateTimeField(default=None, null=True, blank=True)),
            ],
        ),
    ]
