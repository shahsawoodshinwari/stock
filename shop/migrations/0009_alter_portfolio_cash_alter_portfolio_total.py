# Generated by Django 4.1 on 2022-09-23 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_alter_purchase_symbol"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="cash",
            field=models.FloatField(
                default=10000, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="total",
            field=models.FloatField(
                default=10000, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]