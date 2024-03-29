# Generated by Django 5.0.2 on 2024-03-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_socialmediamodel_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMeDescriptionModel",
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
                ("email", models.CharField(max_length=50, verbose_name="ایمیل")),
                (
                    "phone_number",
                    models.CharField(max_length=50, verbose_name="شماره موبایل"),
                ),
                ("address", models.TextField(verbose_name="آدرس")),
            ],
            options={
                "verbose_name": "ارتباط با ما نمایش",
                "verbose_name_plural": "ارتباط با ما نمایش",
            },
        ),
        migrations.AlterModelOptions(
            name="contactmemodel",
            options={
                "verbose_name": "ارتباط با ما نمایش",
                "verbose_name_plural": "ارتباط با ما نمایش",
            },
        ),
        migrations.AlterField(
            model_name="socialmediamodel",
            name="image",
            field=models.ImageField(
                upload_to="social_image", verbose_name="تصویر شبکه اجتماعی"
            ),
        ),
    ]
