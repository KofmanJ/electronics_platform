from rest_framework.exceptions import ValidationError


class SupplierValidator:
    """Проверяет наличие у завода поставщика"""

    def __call__(self, value):
        if value.get('network_level') == 0 and value.get('supplier_name'):
            raise ValidationError('У завода не может быть поставщика')


class SupplierLevelValidator:
    """Проверяет уровень сети поставщика"""

    def __call__(self, value):
        if value.get('supplier_name'):
            if value['network_level'] != value['supplier_name'].network_level + 1:
                raise ValidationError('Уровень поставщика должен быть на 1 выше уровня предыдущего поставщика')
