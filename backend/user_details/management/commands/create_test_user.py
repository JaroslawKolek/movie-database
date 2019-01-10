from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import UserDetails


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Method to quick create test user for development"""
        # TODO: Create endpoint for creating user from form

        username = 'TestUser'
        password = 'asd123'

        user, created = User.objects.get_or_create(username=username)
        user.set_password(password)

        if created:
            UserDetails.objects.create(user=user)

        self.stdout.write(self.style.SUCCESS(
            f"Created user for testing \n Username: '{username}' \n Password: '{password}'"
        ))
