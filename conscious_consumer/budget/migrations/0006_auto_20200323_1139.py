# Generated by Django 3.0.4 on 2020-03-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20200318_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='achievements',
            field=models.PositiveIntegerField(help_text='The number of time periods you have met this goal. Start at 0 - honor system!'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='fails',
            field=models.PositiveIntegerField(help_text='The number of time periods you have missed this goal. Start at 0 - honor system!'),
        ),
    ]
