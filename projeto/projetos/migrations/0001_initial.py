# Generated by Django 5.0.3 on 2024-03-15 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf_rg', models.CharField(max_length=20)),
                ('idade', models.IntegerField()),
                ('endereco', models.CharField(max_length=200)),
                ('nome_responsavel', models.CharField(max_length=100)),
                ('espectro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('valor', models.IntegerField()),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.pergunta')),
            ],
        ),
    ]
