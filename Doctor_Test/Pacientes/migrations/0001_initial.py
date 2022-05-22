# Generated by Django 4.0.3 on 2022-04-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('estado_civil', models.CharField(max_length=200)),
                ('tipo_documento', models.CharField(max_length=200)),
                ('eps', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('alergias', models.BooleanField()),
                ('cirugias', models.BooleanField()),
                ('vacunas', models.BooleanField()),
            ],
        ),
    ]
