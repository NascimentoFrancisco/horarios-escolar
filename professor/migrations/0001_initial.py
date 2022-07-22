# Generated by Django 4.0.6 on 2022-07-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disponibilidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('suap', models.CharField(max_length=100, unique=True)),
                ('coordenador', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=16)),
                ('disponibilidade_professor', models.ManyToManyField(to='disponibilidade.disponibilidade')),
            ],
        ),
    ]
