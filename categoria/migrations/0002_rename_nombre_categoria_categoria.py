# Generated by Django 3.2.20 on 2023-08-15 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='categoria',
        ),
    ]
