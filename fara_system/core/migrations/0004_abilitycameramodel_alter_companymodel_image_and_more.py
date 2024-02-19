# Generated by Django 5.0 on 2024-02-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_servicemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityCameraModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='مدل دوربین')),
                ('ability', models.CharField(max_length=50, verbose_name='قابلیت دوربین')),
            ],
            options={
                'verbose_name': 'قابلیت دوربین',
                'verbose_name_plural': 'قابلیت دوربین ها',
            },
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company_image', verbose_name='تصویر کمپانی'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service_image', verbose_name='تصویر سرویس'),
        ),
        migrations.CreateModel(
            name='CameraModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='شرکت سازنده دوربین')),
                ('title', models.CharField(max_length=40, verbose_name='مدل دوربین')),
                ('image', models.ImageField(blank=True, null=True, upload_to='camera_image', verbose_name='تصویر دوربین')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_image', verbose_name='لوگو شرکت سازنده')),
                ('video', models.FileField(blank=True, null=True, upload_to='video')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='نام کشور سازنده')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('ability', models.ManyToManyField(to='core.abilitycameramodel', verbose_name='قابلیت های دوربین')),
            ],
            options={
                'verbose_name': 'دوربین',
                'verbose_name_plural': 'دوربین ها',
            },
        ),
    ]
