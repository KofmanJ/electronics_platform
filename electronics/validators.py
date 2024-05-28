from rest_framework.exceptions import ValidationError


class SupplierValidator:
    """Проверяет наличие у завода поставщика"""

    def __call__(self, value):
        if value.get('network_level') == 0 and value.get('supplier_name'):
            raise ValidationError('У завода не может быть поставщика')
