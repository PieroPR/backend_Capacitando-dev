# Generated by Django 3.2.20 on 2023-08-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_rename_nombre_categoria_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='estado',
            field=models.IntegerField(default=1, verbose_name='Estado'),
        ),
    ]
