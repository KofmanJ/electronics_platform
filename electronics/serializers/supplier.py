from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from electronics.models import Supplier
from electronics.serializers.contacts import ContactsSerializers
from electronics.serializers.product import ProductSerializers
from electronics.validators import SupplierValidator, SupplierLevelValidator


class SupplierCreateSerializers(serializers.ModelSerializer):
    """ Класс сериализатора cоздания поставщика """
    # network_level = serializers.SerializerMethodField()
    #
    # def get_network_level(self, obj):
    #     if obj.supplier_name:
    #         obj.network_level = obj.supplier_name.network_level + 1
    #         return obj.network_level
    #     else:
    #         return 0

    class Meta:
        model = Supplier
        fields = ['name', 'network_level', 'contact', 'product', 'supplier_name', 'debt',
                  'creation_time']
        validators = [SupplierValidator(), SupplierLevelValidator()]

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['creation_user'] = request.user

        if validated_data.get('supplier_name'):
            supplier_name = validated_data['supplier_name']
            validated_data['network_level'] = supplier_name.network_level + 1

        return super().create(validated_data)


class SupplierSerializers(serializers.ModelSerializer):
    """ Класс сериализатора поставщика """

    contact = ContactsSerializers()
    product = ProductSerializers()

    class Meta:
        model = Supplier
        fields = '__all__'
