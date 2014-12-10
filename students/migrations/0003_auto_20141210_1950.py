# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141210_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='favorite_colour',
            field=models.CharField(default=b'red', max_length=6, choices=[(b'red', b'Red'), (b'orange', b'Orange'), (b'yellow', b'Yellow'), (b'green', b'Green'), (b'blue', b'Blue'), (b'indigo', b'Indigo'), (b'violet', b'Violet')]),
            preserve_default=True,
        ),
    ]
