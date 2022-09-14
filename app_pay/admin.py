from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_editable = ['price']
    search_fields = ['name', 'description']
