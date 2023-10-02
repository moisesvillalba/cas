# Generated by Django 4.2.1 on 2023-09-30 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='user',
            name='documento',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciudades', to='account.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrios', to='account.ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ciudad', verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='user',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.pais', verbose_name='País'),
        ),
    ]