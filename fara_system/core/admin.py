from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['name', 'image_tag']
    
    
class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['name', 'image_tag']
    
    
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CompanyModel, CompanyAdmin)