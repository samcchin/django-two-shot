# Generated by Django 4.2 on 2023-04-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(null=True),
        ),
    ]
