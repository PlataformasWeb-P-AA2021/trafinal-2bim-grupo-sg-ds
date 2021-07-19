# Generated by Django 3.2.4 on 2021-07-18 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('siglas', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=60)),
                ('valorBien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numCuartos', models.IntegerField()),
                ('valorMantenimiento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barriosDepartamento', to='administrativo.barrio')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='administrativo.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=60)),
                ('valorBien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('colorInmueble', models.CharField(max_length=30)),
                ('numCuartos', models.IntegerField()),
                ('numPisos', models.IntegerField()),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barriosCasa', to='administrativo.barrio')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casas', to='administrativo.persona')),
            ],
        ),
    ]