# Generated by Django 4.2.7 on 2023-12-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savedrestaurant",
            name="categories",
            field=models.JSONField(),
        ),
    ]
