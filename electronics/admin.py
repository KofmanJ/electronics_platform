from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import Contacts, Product, Supplier
from .serializers.supplier import SupplierCreateSerializers


@admin.action(description='Очистить задолженность')
def set_null_debt(ModelAdmin, request, queryset):
    """ Действие, очищающее задолженность (меняет поле debt=0) """
    queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """ Админка контактов """
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number', 'creation_user')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Админка продуктов """
    list_display = ('id', 'product_title', 'product_model', 'release_date', 'price', 'creation_user')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """ Админка поставщиков """
    list_display = ('id', 'name', 'network_type', 'level', 'contact', 'product', 'supplier_name', 'debt',
                    'creation_time', 'creation_user')
    list_filter = ('contact__city', 'contact__country')
    actions = [set_null_debt]

    def save_model(self, request, obj, form, change):
        serializer = SupplierCreateSerializers(data=request.POST)
        if serializer.is_valid():
            obj.save()
        else:
            raise ValidationError('Ошибка согласованности полей. Проверьте поля "Уровень поставки", '
                                  '"Тип сети" и "Поставщик"')
