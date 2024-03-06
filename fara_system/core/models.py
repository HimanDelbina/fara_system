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
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    image = models.ImageField(
        null=True, blank=True, upload_to="product_image", verbose_name="تصویر محصول"
    )

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس محصول ها"
        verbose_name = "عکس محصول"


class CompanyModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام کمپانی")
    image = models.ImageField(
        null=True, blank=True, upload_to="company_image", verbose_name="تصویر کمپانی"
    )

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس کمپانی ها در صفحه دوم"
        verbose_name = "عکس کمپانی در صفحه دوم"


class CameraCategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام کمپانی سازنده دوربین")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "عکس کمپانی های سازنده دوربین"
        verbose_name = "عکس کمپانی سازنده دوربین"


class ServiceModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام سرویس")
    image = models.ImageField(
        null=True, blank=True, upload_to="service_image", verbose_name="تصویر سرویس"
    )

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس سرویس ها در صفحه اول"
        verbose_name = "عکس سرویس در صفحه اول"


class AbilityCameraModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="مدل دوربین")
    ability = models.CharField(max_length=50, verbose_name="قابلیت دوربین")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "قابلیت دوربین ها"
        verbose_name = "قابلیت دوربین"


class CameraModel(models.Model):
    # name = models.CharField(max_length=100, verbose_name="شرکت سازنده دوربین")
    category = models.ForeignKey(
        CameraCategoryModel, verbose_name="شرکت سازنده دوربین", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=40, verbose_name="مدل دوربین")
    image = models.ImageField(
        null=True, blank=True, upload_to="camera_image", verbose_name="تصویر دوربین"
    )
    logo = models.ImageField(
        null=True, blank=True, upload_to="logo_image", verbose_name="لوگو شرکت سازنده"
    )
    video = models.FileField(upload_to="video", max_length=100, null=True, blank=True)
    country = models.CharField(
        max_length=30, verbose_name="نام کشور سازنده", null=True, blank=True
    )
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    ability = models.ManyToManyField(
        AbilityCameraModel, verbose_name="قابلیت های دوربین"
    )
    is_publish = models.BooleanField(default=True, verbose_name="آیا نمایش دادده شود ؟")

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    def logo_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.logo.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    logo_tag.short_description = "Logo"
    logo_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "دوربین ها"
        verbose_name = "دوربین"


class ProgramModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام زبان برنامه نویسی")
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="program_image",
        verbose_name="تصویر زبان برنامه نویسی",
    )

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس زبان برنامه نویسی"
        verbose_name = "عکس زبان برنامه نویسی"


class ActivityModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="فعالیت ها")
    description = models.TextField(
        verbose_name="توضیحات فعالیت ها", null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "فعالیت ها"
        verbose_name = "فعالیت ها"


class CardHomeModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="سر تیتر")
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "کادر صفحه اول"
        verbose_name = "کادر صفحه اول"


class SocialMediaModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شبکه اجتماعی")
    link = models.CharField(max_length=50, verbose_name="لینک شبکه اجتماعی")
    image = models.ImageField(
        upload_to="social_image",
        verbose_name="تصویر شبکه اجتماعی",
    )

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(
            '<img src="{}" width="100" height="100"/>'.format(self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    class Meta:
        verbose_name_plural = "عکس شبکه اجتماعی"
        verbose_name = "عکس شبکه اجتماعی"


class ContactMeModel(models.Model):
    username = models.CharField(max_length=50, verbose_name="نام")
    email = models.CharField(max_length=50, verbose_name="ایمیل")
    phone_number = models.CharField(max_length=50, verbose_name="شماره موبایل")
    description = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = "ارتباط با ما"
        verbose_name = "ارتباط با ما"
