# Generated by Django 5.0.3 on 2024-03-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_aluno_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='idade',
            field=models.IntegerField(default=0),
        ),
    ]
