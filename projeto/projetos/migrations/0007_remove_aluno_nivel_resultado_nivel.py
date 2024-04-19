# Generated by Django 5.0.4 on 2024-04-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0006_remove_resultado_nivel_aluno_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='nivel',
        ),
        migrations.AddField(
            model_name='resultado',
            name='nivel',
            field=models.CharField(choices=[('Alto', 'Alto'), ('Médio', 'Médio'), ('Baixo', 'Baixo')], max_length=10, null=True),
        ),
    ]
