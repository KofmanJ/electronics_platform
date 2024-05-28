from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from electronics.models import Supplier
from electronics.serializers.supplier import SupplierCreateSerializers, SupplierSerializers


class SupplierViewSet(ModelViewSet):
    default_serializer = SupplierSerializers
    queryset = Supplier.objects.all()
    serializers = {
        'create': SupplierCreateSerializers,
        'update': SupplierCreateSerializers,
    }
    filter_backends = [filters.SearchFilter]
    search_fields = ['contact__country', ]

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.creation_user = self.request.user
        new_obj.save()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    # def get_permissions(self):
    #     if self.action == 'create':
    #         self.permission_classes = [IsAuthenticated, ~IsModerator]
    #     elif self.action in ['list', 'retrieve', 'update', 'partial_update']:
    #         self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    #     elif self.action == 'destroy':
    #         self.permission_classes = [IsAuthenticated, IsOwner]
    #     return [permission() for permission in self.permission_classes]




