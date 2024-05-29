from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import Contacts, Product, Supplier
from .serializers.supplier import SupplierCreateSerializers


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_model', 'release_date', 'price')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'network_type', 'level', 'contact', 'product', 'supplier_name', 'debt', 'creation_time',
                    'creation_user')
    list_filter = ('contact__city', 'contact__country')

    def save_model(self, request, obj, form, change):
        serializer = SupplierCreateSerializers(data=request.POST)
        if serializer.is_valid():
            obj.save()
        else:
            raise ValidationError('Ошибка согласованности полей. Проверьте поля "Уровень поставки", '
                                  '"Тип сети" и "Поставщик"')
