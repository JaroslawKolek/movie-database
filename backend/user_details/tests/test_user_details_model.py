from django.test import TestCase
from django.contrib.auth.models import User

from user_details.models import UserDetails
from user_details.utils import create_test_user_and_user_details


class UserDetailsModelTestCase(TestCase):
    """ Basic Models tests for UserDetails """

    def setUp(self):
        self.username = "username"
        self.password = "password"
        self.user, self.details = create_test_user_and_user_details(self.username, self.password)

    def test_if_user_created_by_management_command(self):
        self.assertEqual(UserDetails.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)

    def test_if_details_had_empty_movies_fav_list(self):
        self.assertEqual(UserDetails.objects.first().favorites_movies.all().count(), 0)
