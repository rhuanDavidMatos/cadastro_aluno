# Generated by Django 3.2.9 on 2021-11-17 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0002_cursomodel_horas'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.alunomodel')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curso.cursomodel')),
            ],
        ),
    ]