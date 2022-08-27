# Generated by Django 3.0.8 on 2022-08-12 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20210511_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(choices=[('Water', 'Water'), ('Climate', 'Climate'), ('Energy', 'Energy'), ('Land', 'Land'), ('Socio-economic', 'Socio-economic')], max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='satmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='satmodel',
            name='longname',
        ),
        migrations.RemoveField(
            model_name='satmodel',
            name='shortname',
        ),
        migrations.AddField(
            model_name='satmodel',
            name='satellite_or_model',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='satmodel',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Sector'),
        ),
        migrations.AlterField(
            model_name='satmodel',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Unit'),
        ),
    ]
