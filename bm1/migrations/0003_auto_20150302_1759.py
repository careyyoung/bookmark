# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm1', '0002_auto_20150302_1737'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.AlterField(
            model_name='bookmarks1',
            name='url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
