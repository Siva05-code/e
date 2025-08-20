from django.contrib import admin
from .models import Products
from django.utils.html import format_html


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'preview_image')

    def preview_image(self, obj):
        if obj.product_image:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; object-fit:cover;" />',
                obj.product_image.url
            )
        return "No Image"

    preview_image.short_description = "Image Preview"


