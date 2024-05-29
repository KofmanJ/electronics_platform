from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from electronics.models import Supplier
from electronics.serializers.contacts import ContactsSerializers
from electronics.serializers.product import ProductSerializers
from electronics.validators import SupplierValidator


class SupplierCreateSerializers(serializers.ModelSerializer):
    """ Класс сериализатора cоздания поставщика """

    level = serializers.IntegerField(required=False)  # Делаем поле level необязательным

    class Meta:
        model = Supplier
        fields = ['name', 'network_type', 'level', 'contact', 'product', 'supplier_name', 'debt',
                  'creation_time']
        validators = [SupplierValidator()]

    def create(self, value):
        request = self.context.get('request')
        if request and request.user:
            value['creation_user'] = request.user

        if value.get('supplier_name'):
            supplier_name = value['supplier_name']
            value['level'] = supplier_name.level + 1
        elif value.get('network_type') == 0:
            value['level'] = 0

        return super().create(value)


class SupplierSerializers(serializers.ModelSerializer):
    """ Класс сериализатора поставщика """

    contact = ContactsSerializers()
    product = ProductSerializers()
    network_type = serializers.CharField(source='get_network_type_display')

    class Meta:
        model = Supplier
        fields = '__all__'
