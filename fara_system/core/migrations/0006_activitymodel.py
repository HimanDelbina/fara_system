# Generated by Django 5.0 on 2024-02-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_programmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='فعالیت ها')),
                ('description', models.TextField(verbose_name='توضیحات فعالیت ها')),
            ],
            options={
                'verbose_name': 'فعالیت ها',
                'verbose_name_plural': 'فعالیت ها',
            },
        ),
    ]
