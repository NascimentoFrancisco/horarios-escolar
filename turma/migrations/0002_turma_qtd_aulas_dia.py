# Generated by Django 4.0.6 on 2022-07-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='qtd_aulas_dia',
            field=models.IntegerField(default=0),
        ),
    ]