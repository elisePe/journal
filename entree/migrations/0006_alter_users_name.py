# Generated by Django 3.2.23 on 2023-12-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entree', '0005_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]