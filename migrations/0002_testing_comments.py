# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='comments',
            field=models.CharField(default=b'defaultvalue', max_length=500),
        ),
    ]
