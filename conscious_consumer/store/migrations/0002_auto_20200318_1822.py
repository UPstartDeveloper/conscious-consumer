# Generated by Django 3.0.4 on 2020-03-19 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(
                default="",
                help_text="What customers should know.Please include the link, if you're selling on a different website.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Image of the product, if possible.",
                null=True,
                upload_to="images/",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.FloatField(default=0.0, help_text="Cost of product (USD)."),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.OneToOneField(
                default=None,
                help_text="User who posted this product.",
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.CharField(
                blank=True,
                editable=False,
                help_text="Unique URL path to access this product. Generated by the system.",
                max_length=60,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title",
            field=models.CharField(
                default="Product Title",
                help_text="What the product is called.",
                max_length=60,
                unique=True,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "headline",
                    models.CharField(help_text="Main point of review.", max_length=60),
                ),
                (
                    "description",
                    models.TextField(help_text="Full thoughts on product."),
                ),
                (
                    "rating",
                    models.IntegerField(
                        help_text="1 to 5 stars, where 5 is highest rating."
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this product was posted. Automatically generated when the model updates.",
                    ),
                ),
                (
                    "author",
                    models.OneToOneField(
                        help_text="User leaving the review.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Product being reviewed.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="store.Product",
                    ),
                ),
            ],
        ),
    ]
