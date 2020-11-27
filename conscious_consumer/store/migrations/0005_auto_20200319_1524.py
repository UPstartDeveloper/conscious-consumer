# Generated by Django 3.0.4 on 2020-03-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_product_web_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                default="images/question-mark-md.png",
                help_text="Image of the product, if possible.",
                null=True,
                upload_to="images/",
            ),
        ),
    ]
