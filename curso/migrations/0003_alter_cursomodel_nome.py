# Generated by Django 3.2.9 on 2021-11-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_cursomodel_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursomodel',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]