# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('n_flight', models.CharField(max_length=10)),
                ('n_cflight', models.CharField(max_length=10)),
                ('dep_time', models.DateTimeField(null=True, blank=True)),
                ('arr_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('CountryName', models.CharField(max_length=50)),
                ('CityName', models.CharField(max_length=50)),
                ('n_people', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dep_date', models.DateField(blank=True)),
                ('ret_date', models.DateField(blank=True)),
                ('org_1', models.CharField(max_length=20)),
                ('org_2', models.CharField(max_length=20)),
                ('org_3', models.CharField(max_length=20)),
                ('org_4', models.CharField(max_length=20)),
                ('org_5', models.CharField(max_length=20)),
                ('org_6', models.CharField(max_length=20)),
                ('org_7', models.CharField(max_length=20)),
                ('org_8', models.CharField(max_length=20)),
                ('org_9', models.CharField(max_length=20)),
                ('org_10', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dep_date', models.DateField(blank=True)),
                ('ret_date', models.DateField(blank=True)),
                ('n_psgrs', models.IntegerField(default=0)),
                ('n_orgs', models.IntegerField(default=0)),
                ('flights', models.ManyToManyField(to='f2m_app.Flight')),
                ('places', models.ManyToManyField(to='f2m_app.Place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='flight',
            name='stations',
            field=models.ManyToManyField(to='f2m_app.Place'),
            preserve_default=True,
        ),
    ]
