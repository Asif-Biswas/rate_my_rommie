# Generated by Django 4.2.6 on 2023-10-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="roommate",
            name="email",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="roommate",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
