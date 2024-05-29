from rest_framework import serializers

from electronics.models import Product


class ProductSerializers(serializers.ModelSerializer):
    """ Класс сериализатора продукта """

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'creation_user': {'required': False}  # делаем поле creation_user необязательным
        }

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['creation_user'] = request.user
        return super().create(validated_data)
