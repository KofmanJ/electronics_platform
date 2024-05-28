from rest_framework import status
from rest_framework.test import APITestCase

from electronics.models import Contacts, Product, Supplier
from users.models import User


class ContactTestCase(APITestCase):

    def setUp(self):

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
            house_number=''
        )

    def test_contact_list(self):
        """Тестирование получения списка контактов"""

        # self.client.force_authenticate(user=self.user)

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
            [
                {
                    'id': self.contact.id,
                    'email': self.contact.email,
                    'country': self.contact.country,
                    'city': self.contact.city,
                    'street': self.contact.street,
                    'house_number': self.contact.house_number,
                }
            ]
        )

    def test_contact_retrieve(self):
        """Тестирование получения контакта"""

        # self.client.force_authenticate(user=self.user)

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
            [
                {
                    'id': self.contact.id,
                    'email': self.contact.email,
                    'country': self.contact.country,
                    'city': self.contact.city,
                    'street': self.contact.street,
                    'house_number': self.contact.house_number,
                }
            ]
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
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_contact_update(self):
        """Тестирование обновления пользователя"""

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

        self.user = User.objects.create(
            email='testtest@test.ru',
            password='testtest'
        )

        self.client.force_authenticate(user=self.user)

        self.product = Product.objects.create(
            product_title='Машина тестомесильная',
            product_model='GRTE-123',
            release_date='2020-01-01',
            price=1000
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
            [
                {
                    'id': self.product.id,
                    'product_title': self.product.product_title,
                    'product_model': self.product.product_model,
                    'release_date': self.product.release_date,
                    'price': self.product.price
                }
            ]
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
            [
                {
                    'id': self.product.id,
                    'product_title': self.product.product_title,
                    'product_model': self.product.product_model,
                    'release_date': self.product.release_date,
                    'price': self.product.price
                }
            ]
        )

    def test_product_create(self):
        """Тестирование создания продукта"""

        response = self.client.post(
            '/product/',
            data={
                'product_title': 'Машина отсадочная',
                'product_model': 'FBK-9000',
                'release_date': '2023-11-01',
                'price': 12500
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
            house_number=''
        )

        self.product = Product.objects.create(
            product_title='Машина тестомесильная',
            product_model='GRTE-123',
            release_date='2020-01-01',
            price=1000
        )

        self.supplier = Supplier.objects.create(
            name='Test supplier',
            network_level=1,
            contact=self.contact,
            product=self.product,
            debt=0,
            creation_user=self.user
        )

    def test_supplier_list(self):
        """Тестирование получения списка поставщиков"""

        response = self.client.get(
            '/supplier/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_supplier_retrieve(self):
        """Тестирование получения поставщика"""

        response = self.client.get(
            '/supplier/', kwargs={'pk': self.supplier.pk}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_supplier_create(self):
        """Тестирование создания поставщика"""

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'network_level': 1,
                'contact': self.contact.pk,
                'product': self.product.pk,
                'debt': 0,
                'creation_user': self.user.pk
            }
        )

        # print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_supplier_create_validate(self):
        """Тестирование создания поставщика, когда валидация не проходит"""

        response = self.client.post(
            '/supplier/',
            data={
                'name': 'Test supplier',
                'network_level': 0,
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
            {'non_field_errors': ['У завода не может быть поставщика']}
        )

    def test_supplier_update(self):
        """Тестирование обновления поставщика"""

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
        """Тестирование удаления поставщика"""

        response = self.client.delete(
            f'/supplier/{self.supplier.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
