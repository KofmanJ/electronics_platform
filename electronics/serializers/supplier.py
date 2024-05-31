from rest_framework import serializers

from electronics.models import Supplier
from electronics.serializers.contacts import ContactsSerializers
from electronics.serializers.product import ProductSerializers
from electronics.validators import SupplierValidator


class SupplierCreateSerializers(serializers.ModelSerializer):
    """ Класс сериализатора для cоздания поставщика """

    level = serializers.IntegerField(required=False)  # Делаем поле level необязательным

    class Meta:
        model = Supplier
        fields = ['name', 'network_type', 'level', 'contact', 'product', 'supplier_name', 'debt',
                  'creation_time']
        validators = [SupplierValidator()]

    def create(self, validated_data):
        """ Метод создания поставщика """
        request = self.context.get('request')
        if request and request.user:
            validated_data['creation_user'] = request.user

        if validated_data.get('supplier_name'):
            supplier_name = validated_data['supplier_name']
            validated_data['level'] = supplier_name.level + 1
        elif validated_data.get('network_type') == 0:
            validated_data['level'] = 0

        return super().create(validated_data)


class SupplierSerializers(serializers.ModelSerializer):
    """ Класс сериализатора поставщика """

    contact = ContactsSerializers(read_only=True)
    product = ProductSerializers(read_only=True)
    network_type = serializers.CharField(source='get_network_type_display')

    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt', 'creation_time', 'creation_user', )

    def validate(self, data):
        """ Метод валидации поставщика """
        print(data)
        request = self.context.get('request')
        if not request.user.is_superuser:
            if self.instance and any(field in data for field in ["level", "get_network_type_display", "supplier_name"]):
                raise serializers.ValidationError(
                    "Обновление данных полей запрещено. "
                    "Обратитесь к администратору сайта, если вам необходимо изменить данные.")

        return data
