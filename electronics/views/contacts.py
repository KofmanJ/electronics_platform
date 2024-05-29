from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics.models import Contacts
from electronics.paginators import ElectronicsPagination
from electronics.serializers.contacts import ContactsSerializers


class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ElectronicsPagination
