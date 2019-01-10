from django.test import TestCase
from django.contrib.auth.models import User
from django.core.management import call_command

from ..models import UserDetails


class UserDetailsModelTestCase(TestCase):
    """ Basic Models tests for UserDetails """

    def setUp(self):
        call_command('create_test_user')

    def test_if_user_created_by_management_command(self):
        self.assertEqual(UserDetails.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)

    def test_if_details_had_empty_movies_fav_list(self):
        self.assertEqual(UserDetails.objects.first().favorites_movies.all().count(), 0)
