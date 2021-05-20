# Generated by Django 3.1.7 on 2021-04-01 07:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=100)),
                ('longname', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SatModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, max_length=100)),
                ('shortname', models.CharField(max_length=100)),
                ('longname', models.CharField(max_length=400)),
                ('sensor', models.CharField(blank=True, max_length=400)),
                ('product', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=datetime.datetime(2021, 4, 1, 7, 22, 57, 317541))),
                ('sector', models.CharField(choices=[('Water', 'Water'), ('Climate', 'Climate'), ('Energy', 'Energy'), ('Land', 'Land'), ('Socio-economic', 'Socio-economic')], max_length=400)),
                ('reference', models.URLField(max_length=400)),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.variables')),
            ],
        ),
    ]
