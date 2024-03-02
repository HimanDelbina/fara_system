# Generated by Django 5.0.2 on 2024-03-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_cardhomemodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialMediaModel",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="نام شبکه اجتماعی"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="program_image", verbose_name="تصویر شبکه اجتماعی"
                    ),
                ),
            ],
            options={
                "verbose_name": "عکس شبکه اجتماعی",
                "verbose_name_plural": "عکس شبکه اجتماعی",
            },
        ),
    ]
