from rest_framework import status
from rest_framework.test import APITestCase

from electronics.models import Contacts, Product, Supplier
from users.models import User


class ContactTestCase(APITestCase):
    """ Тестирование контактов """

    def setUp(self):
        """Подготовка данных для тестирования"""

        self.user = User.objects.create(
            email='testtest@test.ru',
            password='testtest'
        )

        self.client.force_authenticate(user=self.user)

        self.contact = Contacts.objects.create(
            email='testtest@test.ru',
            country='Russia',
            city='Moscow',
            street='',
            house_number='',
            creation_user=self.user
        )

    def test_contact_list(self):
        """Тестирование получения списка контактов"""

        response = self.client.get(
            '/contact/'
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.contact.id,
                            'email': self.contact.email,
                            'country': self.contact.country,
                            'city': self.contact.city,
                            'street': self.contact.street,
                            'house_number': self.contact.house_number,
                            'creation_user': self.user.id
                        }
                    ]
            }
        )

    def test_contact_retrieve(self):
        """Тестирование получения контакта"""

        response = self.client.get(
            '/contact/', kwargs={'pk': self.contact.pk}
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.contact.id,
                            'email': self.contact.email,
                            'country': self.contact.country,
                            'city': self.contact.city,
                            'street': self.contact.street,
                            'house_number': self.contact.house_number,
                            'creation_user': self.user.id
                        }
                    ]
            }
        )

    def test_contact_create(self):
        """Тестирование создания контакта"""

        response = self.client.post(
            '/contact/',
            data={
                'email': 'test1test1@test.ru',
                'country': 'USA',
                'city': 'New York',
                'street': '',
                'house_number': '',
                'creation_user': self.user.id
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_contact_update(self):
        """Тестирование обновления контакта"""

        updated_data = {
            'city': 'Saint Petersburg',
        }

        response = self.client.patch(
            f'/contact/{self.contact.pk}/',
            data=updated_data
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_contact_delete(self):
        """Тестирование удаления пользователя"""

        response = self.client.delete(
            f'/contact/{self.contact.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class ProductTestCase(APITestCase):

    def setUp(self):
        """Подготовка данных для тестирования"""

        self.user = User.objects.create(
            email='testtest@test.ru',
            password='testtest'
        )

        self.client.force_authenticate(user=self.user)

        self.product = Product.objects.create(
            product_title='Машина тестомесильная',
            product_model='GRTE-123',
            release_date='2020-01-01',
            price=1000,
            creation_user=self.user
        )

    def test_product_list(self):
        """Тестирование получения списка продуктов"""

        response = self.client.get(
            '/product/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.product.id,
                            'product_title': self.product.product_title,
                            'product_model': self.product.product_model,
                            'release_date': self.product.release_date,
                            'price': self.product.price,
                            'creation_user': self.user.id
                        }
                    ]
            }
        )

    def test_product_retrieve(self):
        """Тестирование получения продукта"""

        response = self.client.get(
            '/product/', kwargs={'pk': self.product.pk}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.product.id,
                            'product_title': self.product.product_title,
                            'product_model': self.product.product_model,
                            'release_date': self.product.release_date,
                            'price': self.product.price,
                            'creation_user': self.user.id
                        }
                    ]
            }
        )

    def test_product_create(self):
        """Тестирование создания продукта"""

        response = self.client.post(
            '/product/',
            data={
                'product_title': 'Машина отсадочная',
                'product_model': 'FBK-9000',
                'release_date': '2023-11-01',
                'price': 12500,
                'creation_user': self.user.id
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_product_update(self):
        """Тестирование обновления продукта"""

        updated_data = {
            'product_model': 'FBK-8000',
        }

        response = self.client.patch(
            f'/product/{self.product.pk}/',
            data=updated_data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_product_delete(self):
        """Тестирование удаления продукта"""

        response = self.client.delete(
            f'/product/{self.product.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SupplierTestCase(APITestCase):

    def setUp(self):
        """Подготовка данных для тестирования"""

        self.user = User.objects.create(
            email='testtest@test.ru',
            password='testtest'
        )

        self.user_admin = User.objects.create(
            email='admin@test.ru',
            password='adminadmin',
            is_superuser=True
        )

        # self.client.force_authenticate(user=self.user)

        self.contact = Contacts.objects.create(
            email='testtest@test.ru',
            country='Russia',
            city='Moscow',
            street='',
            house_number='',
            creation_user=self.user
        )

        self.product = Product.objects.create(
            product_title='Машина тестомесильная',
            product_model='GRTE-123',
            release_date='2020-01-01',
            price=1000,
            creation_user=self.user
        )

        self.supplier = Supplier.objects.create(
            name='Test supplier',
            network_type=0,
            level=0,
            contact=self.contact,
            product=self.product,
            debt=0,
            creation_user=self.user
        )

    def test_supplier_list(self):
        """Тестирование получения списка поставщиков"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/supplier/'
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_supplier_retrieve(self):
        """Тестирование получения поставщика"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/supplier/', kwargs={'pk': self.supplier.pk}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_supplier_create(self):
        """Тестирование создания поставщика"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'network_type': 1,
                'contact': self.contact.pk,
                'product': self.product.pk,
                'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_supplier_update(self):
        """Тестирование обновления поставщика"""

        self.client.force_authenticate(user=self.user)

        updated_data = {
            'name': 'Test suppliers',
        }

        response = self.client.patch(
            f'/supplier/{self.supplier.pk}/',
            data=updated_data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_supplier_delete(self):
        """Тестирование удаления поставщика админом"""

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/supplier/{self.supplier.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_supplier_delete_admin(self):
        """Тестирование удаления поставщика админом"""

        self.client.force_authenticate(user=self.user_admin)

        response = self.client.delete(
            f'/supplier/{self.supplier.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_supplier_create_validate_1(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                # 'level': 0,
                'network_type': 0,
                'contact': self.contact.pk,
                'product': self.product.pk,
                'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['У завода не может быть поставщика. '
                                  'Выберете корректный тип сети или удалите поставщика.']}
        )

    def test_supplier_create_validate_2(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                # 'level': 0,
                # 'network_type': 0,
                'contact': self.contact.pk,
                'product': self.product.pk,
                # 'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Для создания поставщика укажите поставщика и тип сети. '
                                  'Если вы являетесь заводом, укажите тип сети - 0.']}
        )

    def test_supplier_create_validate_3(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'level': 0,
                'network_type': 1,
                'contact': self.contact.pk,
                'product': self.product.pk,
                'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['На нулевом уровне поставки может находиться только завод. '
                                  'Выберете корректный тип сети или удалите поставщика.']}
        )

    def test_supplier_create_validate_4(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                # 'level': 0,
                'network_type': 1,
                'contact': self.contact.pk,
                'product': self.product.pk,
                # 'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Для создания записи укажите вашего поставщика. '
                                  'Если вы являетесь заводом, укажите тип сети - 0.']}
        )

    def test_supplier_create_validate_5(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'level': 1,
                'network_type': 0,
                'contact': self.contact.pk,
                'product': self.product.pk,
                # 'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Вы выбрали тип сети завод - 0. '
                                  'Если вы являетесь заводом, в цепочке поставок вы можете иметь только уровень - 0. '
                                  'Для создания записи вы можете сделать следующее: '
                                  '1. Не указывайте уровень и поставщика, либо укажите уровень в цепочке поставки - 0. '
                                  '2. Если не вы являетесь заводом, укажите вашего поставщика и тип сети.']}
        )

    def test_supplier_create_validate_6(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'level': 1,
                # 'network_type': 0,
                'contact': self.contact.pk,
                'product': self.product.pk,
                'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Для создания поставщика укажите тип вашей сети.']}
        )

    def test_supplier_create_validate_7(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'level': 0,
                'network_type': 1,
                'contact': self.contact.pk,
                'product': self.product.pk,
                'supplier_name': self.supplier.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['На нулевом уровне поставки может находиться только завод. '
                                  'Выберете корректный тип сети или удалите поставщика.']}
        )
