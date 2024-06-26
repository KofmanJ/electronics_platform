from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        """Подготовка данных для тестирования"""

        self.user = User.objects.create(
            first_name='user',
            last_name='user',
            email='user@test.ru',
            password='testtest'
        )

        self.user_admin = User.objects.create(
            first_name='admin',
            last_name='admin',
            email='admin@test.ru',
            password='adminadmin',
            is_superuser=True
        )

    def test_create_user(self):
        """Тестирование создания пользователя"""

        response = self.client.post(
            reverse('users:users_create'),
            data={
                'first_name': 'test1',
                'last_name': '',
                'email': 'test1@test.ru',
                'password': 'test1'
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_user(self):
        """Тестирование получения списка пользователей"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('users:users_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_list_user_admin(self):
        """Тестирование получения списка пользователей администратором"""

        self.client.force_authenticate(user=self.user_admin)

        response = self.client.get(
            reverse('users:users_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [
                {
                    'id': self.user.id,
                    'first_name': self.user.first_name,
                    'last_name': self.user.last_name,
                    'email': self.user.email,
                    'is_active': self.user.is_active
                },
                {
                    'id': self.user_admin.id,
                    'first_name': self.user_admin.first_name,
                    'last_name': self.user_admin.last_name,
                    'email': self.user_admin.email,
                    'is_active': self.user_admin.is_active
                }
            ]
        )

    def test_update_user(self):
        """Тестирование обновления пользователя"""

        updated_data = {
            'first_name': 'test2',
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            reverse('users:users_update', kwargs={'pk': self.user.pk}),
            data=updated_data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_user(self):
        """Тестирование получения пользователя"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('users:users_retrieve', kwargs={'pk': self.user.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': self.user.id,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
                'is_active': self.user.is_active
            }
        )

    def test_delete_user(self):
        """Тестирование удаления пользователя"""

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('users:users_destroy', kwargs={'pk': self.user.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
