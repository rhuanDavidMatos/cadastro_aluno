# Generated by Django 3.2.9 on 2021-11-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_alter_enderecomodel_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enderecomodel',
            name='cep',
            field=models.CharField(max_length=8),
        ),
    ]