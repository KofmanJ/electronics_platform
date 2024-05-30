from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics.models import Contacts
from electronics.paginators import ElectronicsPagination
from electronics.serializers.contacts import ContactsSerializers
from users.permissions import IsOwner, IsModerator, IsSuperUser


class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()
    pagination_class = ElectronicsPagination

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.creation_user = self.request.user
        new_obj.save()

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner | IsSuperUser]
        return [permission() for permission in self.permission_classes]
