from rest_framework import serializers

from electronics.models import Supplier
from electronics.serializers.contacts import ContactsSerializers
from electronics.serializers.product import ProductSerializers
from electronics.validators import SupplierValidator


class SupplierCreateSerializers(serializers.ModelSerializer):
    """ Класс сериализатора cоздания поставщика """

    class Meta:
        model = Supplier
        fields = ['name', 'network_level', 'contact', 'product', 'supplier_name', 'debt', 'creation_user',
                  'creation_time']
        validators = [SupplierValidator()]


class SupplierSerializers(serializers.ModelSerializer):
    """ Класс сериализатора поставщика """

    class Meta:
        model = Supplier
        fields = '__all__'
