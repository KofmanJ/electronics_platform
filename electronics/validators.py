from rest_framework.exceptions import ValidationError


class SupplierValidator:
    """Проверка валидации поставщика"""

    def __call__(self, value):
        if value.get('network_type') == 0 and value.get('supplier_name'):
            raise ValidationError('У завода не может быть поставщика. '
                                  'Выберете корректный тип сети или удалите поставщика.'
                                  )

        if value.get('network_type') != 0 and value.get('level') == 0 and value.get('supplier_name') != 0:
            raise ValidationError('На нулевом уровне поставки может находиться только завод. '
                                  'Выберете корректный тип сети или удалите поставщика.'
                                  )

        if value.get('supplier_name') and value.get('level') is not None:
            if value.get('level') != value['supplier_name'].level + 1:
                raise ValidationError(
                    'Уровень поставщика должен быть на 1 выше уровня вашего поставщика. '
                    'Вы можете не выставлять уровень вручную, программа сделает это автоматически.'
                )

        if value.get('level') is None and value.get('supplier_name') is None and value.get('network_type') is None:
            raise ValidationError(
                'Для создания поставщика укажите поставщика и тип сети. '
                'Если вы являетесь заводом, укажите тип сети - 0.'
            )

        if value.get('network_type') != 0 and value.get('level') is None and value.get('supplier_name') is None:
            raise ValidationError(
                'Для создания записи укажите вашего поставщика. '
                'Если вы являетесь заводом, укажите тип сети - 0.'
            )

        if value.get('network_type') == 0 and value.get('level') != 0 and value.get('level') is not None:
            raise ValidationError(
                'Вы выбрали тип сети завод - 0. '
                'Если вы являетесь заводом, в цепочке поставок вы можете иметь только уровень - 0. '
                'Для создания записи вы можете сделать следующее: '
                '1. Не указывайте уровень и поставщика, либо укажите уровень в цепочке поставки - 0. '
                '2. Если не вы являетесь заводом, укажите вашего поставщика и тип сети.'
            )

        if value.get('network_type') is None and value.get('level') != 0 and value.get('supplier_name'):
            raise ValidationError(
                'Для создания поставщика укажите тип вашей сети.'
            )

        if value.get('level') == 0 and value.get('network_type') != 0:
            raise ValidationError('На нулевом уровне поставки может быть только завод. '
                                  'Если вы являетесь заводом, укажите тип сети - 0.'
                                  )

        if value.get('network_type') != 0 and value.get('level') != 0 and value.get('supplier_name') is None:
            raise ValidationError('Вы указали тип сети, не являющегося заводом. '
                                  'Если вы не являетесь заводом, укажите вашего поставщика.'
                                  )

        if value.get('network_type') == 0 and value.get('debt') is not None:
            raise ValidationError('У завода не может быть задолженности. '
                                  'Если вы являетесь заводом, оставьте поле задолженности пустым.'
                                  )
