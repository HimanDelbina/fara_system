# Generated by Django 5.0.2 on 2024-02-24 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_activitymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramodel',
            name='is_publish',
            field=models.BooleanField(default=True, verbose_name='آیا نمایش دادده شود ؟'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات فعالیت ها'),
        ),
        migrations.AlterField(
            model_name='cameramodel',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.companymodel', verbose_name='شرکت سازنده دوربین'),
        ),
    ]