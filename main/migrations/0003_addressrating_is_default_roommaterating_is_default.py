# Generated by Django 4.2.6 on 2023-10-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_roommate_email_alter_roommate_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="addressrating",
            name="is_default",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="roommaterating",
            name="is_default",
            field=models.BooleanField(default=False),
        ),
    ]