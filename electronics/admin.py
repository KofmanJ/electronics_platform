from django.contrib import admin
from .models import Contacts, Product, Supplier


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_model', 'release_date', 'price')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'network_level', 'contact', 'product', 'supplier_name', 'debt', 'creation_time',
                    'creation_user')
    list_filter = ('contact__city', 'contact__country')
