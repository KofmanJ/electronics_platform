from rest_framework import serializers

from electronics.models import Contacts


class ContactsSerializers(serializers.ModelSerializer):
    """ Класс сериализатора контактов """

    class Meta:
        model = Contacts
        fields = '__all__'
