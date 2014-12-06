# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('technology', models.CharField(max_length=2, choices=[(b'PY', b'Python'), (b'RU', b'Ruby'), (b'JS', b'JavaScript')])),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
                ('assistant', models.ForeignKey(related_name='course_assistant', blank=True, to='coaches.Coach')),
                ('lecturer', models.ForeignKey(to='coaches.Coach')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
