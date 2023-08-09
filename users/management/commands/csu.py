from django.core.management import BaseCommand
from users.models import User
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='13@mail.ru',
            first_name='Admin',
            last_name='SuperUser',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456')
        user.save()