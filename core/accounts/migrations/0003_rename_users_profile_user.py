# Generated by Django 3.2.23 on 2023-11-12 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="users",
            new_name="user",
        ),
    ]
