# Generated by Django 4.1.2 on 2022-11-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('documento', models.CharField(max_length=100, unique=True, verbose_name='Documento de identidad')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('egresado_ufps', models.BooleanField(default=False, verbose_name='¿es egresado de la UFPS?')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código de egresado')),
                ('es_extranjero', models.BooleanField(default=False, verbose_name='Extranjero')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=50, verbose_name='Tipo de documento')),
            ],
        ),
    ]