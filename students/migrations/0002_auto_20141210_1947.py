# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite_colour', models.CharField(default=b'red', max_length=1, choices=[(b'red', b'Red'), (b'orange', b'Orange'), (b'yellow', b'Yellow'), (b'green', b'Green'), (b'blue', b'Blue'), (b'indigo', b'Indigo'), (b'violet', b'Violet')])),
                ('address', models.ForeignKey(to='students.Address')),
                ('unloved_courses', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Standard'), (b'G', b'Gold'), (b'V', b'Vip')]),
            preserve_default=True,
        ),
    ]
