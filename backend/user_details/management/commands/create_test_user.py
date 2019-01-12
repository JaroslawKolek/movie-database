from django.core.management.base import BaseCommand
from user_details.utils import create_test_user_and_user_details


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help="User's login")
        parser.add_argument('password', type=str, help="User's password")

    def handle(self, *args, **options):
        """Method to quick create test user for development"""
        username = options["username"]
        password = options["password"]
        create_test_user_and_user_details(username, password)

        self.stdout.write(self.style.SUCCESS(
            f"Created user for testing \n Username: '{username}' \n Password: '{password}'"
        ))
