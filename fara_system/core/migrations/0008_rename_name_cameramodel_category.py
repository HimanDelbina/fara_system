# Generated by Django 5.0.2 on 2024-02-24 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cameramodel_is_publish_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cameramodel',
            old_name='name',
            new_name='category',
        ),
    ]
