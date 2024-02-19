from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['name', 'image_tag']
    
class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['name', 'image_tag']
    
class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['name', 'image_tag']
    
class AbilityCameraAdmin(admin.ModelAdmin):
    fields = ['name', 'ability']
    list_display = ['name', 'ability']
    
class CameraAdmin(admin.ModelAdmin):
    fields = ['name','title', 'image', 'logo' , 'video' ,'country','description','ability']
    list_display = ['name','title', 'image_tag','logo_tag']
    
    
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CompanyModel, CompanyAdmin)
admin.site.register(ServiceModel, ServiceAdmin)
admin.site.register(CameraModel, CameraAdmin)
admin.site.register(AbilityCameraModel, AbilityCameraAdmin)