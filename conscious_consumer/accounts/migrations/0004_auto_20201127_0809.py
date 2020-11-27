# Generated by Django 3.0.4 on 2020-11-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_auto_20201127_0752"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="mugshot",
            field=models.ImageField(
                default="images/user-icon.jpg",
                help_text="User profile image",
                upload_to="images/",
            ),
        ),
    ]
