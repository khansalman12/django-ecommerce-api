from urllib.parse import urlencode
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from django.urls import reverse
from . import models
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['title' , 'unit_price', 'inventory_status', 'collection','description']
    list_editable = ['unit_price']
    list_per_page = 10
    @admin.display(ordering='inventory')
    def inventory_status (self, product):
        if product.inventory < 10:
            return 'low'
        return 'normal'

# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'placed_at', 'customer']
    list_editable = ['customer']
    list_per_page = 15


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    # def product_count(self, collection):
    #
    #     }))
    #     return format_html('<a href="{ }">{}</a>', collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product') )



