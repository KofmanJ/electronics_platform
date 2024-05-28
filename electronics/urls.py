from rest_framework import routers

from electronics.apps import ElectronicsConfig
from electronics.views.contacts import ContactsViewSet
from electronics.views.product import ProductViewSet
from electronics.views.supplier import SupplierViewSet

app_name = ElectronicsConfig.name

router = routers.SimpleRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactsViewSet, basename='contact')


urlpatterns = router.urls
