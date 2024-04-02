# Generated by Django 4.1 on 2024-04-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('homme', 'Homme'), ('femme', 'Femme')], max_length=10, null=True, verbose_name='Sexe'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name="Nom d'utilisateur"),
        ),
    ]
