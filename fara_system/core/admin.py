from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "image",
    ]
    list_display = [
        "name",
        "image_tag",
    ]


class CompanyAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "image",
    ]
    list_display = [
        "name",
        "image_tag",
    ]


class ServiceAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "image",
    ]
    list_display = [
        "name",
        "image_tag",
    ]


class ProgramAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "image",
    ]
    list_display = [
        "name",
        "image_tag",
    ]


class SocialMediaAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "link",
        "image",
    ]
    list_display = [
        "name",
        "link",
        "image_tag",
    ]


class AbilityCameraAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "ability",
    ]
    list_display = [
        "name",
        "ability",
    ]


class ActivityAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "description",
    ]
    list_display = [
        "name",
    ]


class CardHomeAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "description",
    ]
    list_display = [
        "name",
        "description",
    ]


class CameraCategoryAdmin(admin.ModelAdmin):
    fields = [
        "name",
    ]
    list_display = [
        "name",
    ]


class ContactMeAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "email",
        "phone_number",
        "description",
    ]
    list_display = [
        "username",
        "email",
        "phone_number",
    ]


class CameraAdmin(admin.ModelAdmin):
    fields = [
        "category",
        "title",
        "image",
        "logo",
        "video",
        "country",
        "description",
        "ability",
    ]
    list_display = [
        "title",
        "category",
        "image_tag",
        "logo_tag",
    ]

    def camera_name(self, instance):
        return instance.category.name


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CompanyModel, CompanyAdmin)
admin.site.register(ServiceModel, ServiceAdmin)
admin.site.register(CameraModel, CameraAdmin)
admin.site.register(AbilityCameraModel, AbilityCameraAdmin)
admin.site.register(ProgramModel, ProgramAdmin)
admin.site.register(ActivityModel, ActivityAdmin)
admin.site.register(CameraCategoryModel, CameraCategoryAdmin)
admin.site.register(CardHomeModel, CardHomeAdmin)
admin.site.register(SocialMediaModel, SocialMediaAdmin)
admin.site.register(ContactMeModel, ContactMeAdmin)
