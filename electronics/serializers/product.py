from rest_framework import serializers

from electronics.models import Product


class ProductSerializers(serializers.ModelSerializer):
    """ Класс сериализатора продукта """

    class Meta:
        model = Product
        fields = '__all__'
