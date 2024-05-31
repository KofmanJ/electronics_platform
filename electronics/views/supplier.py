from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics.models import Supplier
from electronics.paginators import ElectronicsPagination
from electronics.serializers.supplier import SupplierCreateSerializers, SupplierSerializers
from users.permissions import IsOwner, IsModerator, IsSuperUser


class SupplierViewSet(ModelViewSet):
    default_serializer = SupplierSerializers
    queryset = Supplier.objects.all()
    serializers = {
        'create': SupplierCreateSerializers,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact__country']
    pagination_class = ElectronicsPagination

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.creation_user = self.request.user
        new_obj.save()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_queryset(self):
        user = self.request.user
        obj = super().get_queryset()
        if user.groups.filter(name='moderator').exists() or user.is_superuser:
            return obj
        return obj.filter(creation_user=user)

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsSuperUser]
        return [permission() for permission in self.permission_classes]
