# Generated by Django 5.1.3 on 2024-11-15 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "Driver"},
        ),
        migrations.RenameField(
            model_name="car",
            old_name="driver",
            new_name="drivers",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="manufacture",
            new_name="manufacturer",
        ),
    ]