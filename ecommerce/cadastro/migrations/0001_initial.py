# Generated by Django 4.1.3 on 2022-12-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cpf', models.IntegerField()),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
