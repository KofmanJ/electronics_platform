from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='juliakofmana@gmail.com',
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('j3h7k2')
        user.save()


# User2
# email='jk@mail.ru',
# password='j3h7k2'

# User2
# email='testtest@mail.ru',
# password='123123'
