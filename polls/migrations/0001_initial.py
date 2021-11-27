# Generated by Django 3.2.5 on 2021-11-03 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_texto', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('votos_totales', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Opciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion_texto', models.CharField(max_length=150)),
                ('votos', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pregunta')),
            ],
        ),
    ]