# Generated by Django 5.1.2 on 2024-12-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(default='Inconnu', max_length=100),
        ),
    ]
