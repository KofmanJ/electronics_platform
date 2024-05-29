from django.conf import settings
from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}

network_type = [
    (0, "Завод"),
    (1, "Розничная сеть"),
    (2, "Индивидуальный предприниматель"),
]


class Contacts(models.Model):
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=150, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    product_title = models.CharField(max_length=200, verbose_name='Название продукта')
    product_model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода', **NULLABLE)
    price = models.FloatField(verbose_name='Цена', **NULLABLE)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    network_type = models.IntegerField(choices=network_type, verbose_name='Тип сети', default=0)
    level = models.PositiveIntegerField(verbose_name='Уровень поставки')
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    supplier_name = models.ForeignKey('Supplier', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность', **NULLABLE)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    creation_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
