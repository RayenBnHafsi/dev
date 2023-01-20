from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20

