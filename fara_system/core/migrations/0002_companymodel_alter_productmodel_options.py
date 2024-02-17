# Generated by Django 5.0.2 on 2024-02-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyModel",
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
                ("name", models.CharField(max_length=100, verbose_name="نام کمپانی")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="project_image",
                        verbose_name="تصویر کمپانی",
                    ),
                ),
            ],
            options={
                "verbose_name": "عکس کمپانی در صفحه دوم",
                "verbose_name_plural": "عکس کمپانی ها در صفحه دوم",
            },
        ),
        migrations.AlterModelOptions(
            name="productmodel",
            options={
                "verbose_name": "عکس محصول",
                "verbose_name_plural": "عکس محصول ها",
            },
        ),
    ]
