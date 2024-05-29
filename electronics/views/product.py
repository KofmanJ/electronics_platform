from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics.models import Product
from electronics.paginators import ElectronicsPagination
from electronics.serializers.product import ProductSerializers


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ElectronicsPagination

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.creation_user = self.request.user
        new_obj.save()
