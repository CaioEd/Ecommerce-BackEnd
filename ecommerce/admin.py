from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'image_tag')
    search_fields = ('name', 'description')

    def image_tag(self, obj):
        if obj.image:
            "ok"
        return "No Image"
    
    image_tag.short_description = 'Image'  # Define o nome da coluna no Django Admin