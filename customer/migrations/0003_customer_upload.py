# Generated by Django 4.1.3 on 2023-02-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_customers_cust_gender"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer_upload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.TextField(max_length=100)),
                ("customer_contact", models.TextField(max_length=10)),
                ("customer_image", models.ImageField(upload_to="profile/")),
            ],
        ),
    ]
