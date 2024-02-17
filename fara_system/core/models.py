from django.db import models
import os
from django.utils.html import mark_safe
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def news_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"image/{final_name}"
    return x

class ProductModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    image = models.ImageField(
        null=True, blank=True, upload_to='project_image', verbose_name='تصویر محصول')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس محصول ها"
        verbose_name = "عکس محصول"
        
        
class CompanyModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام کمپانی')
    image = models.ImageField(
        null=True, blank=True, upload_to='project_image', verbose_name='تصویر کمپانی')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس کمپانی ها در صفحه دوم"
        verbose_name = "عکس کمپانی در صفحه دوم"