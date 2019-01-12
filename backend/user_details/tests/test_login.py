from django.shortcuts import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from user_details.utils import create_test_user_and_user_details


class UserLoginTestCase(APITestCase):
    """ Test User login endpoint """

    def setUp(self):
        self.username = "username"
        self.password = "password"
        self.user, self.details = create_test_user_and_user_details(self.username, self.password)

    def test_login_with_correct_credentials(self):
        response = self._login(self.username, self.password)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), Token.objects.all()[0].key)

    def test_login_with_incorrect_credentials(self):
        response = self._login(self.username, 'wrong_password')
        self.assertEqual(response.status_code, 400)

    def _login(self, username, password):
        url = reverse('user_details:login')
        return self.client.post(url, data={'username': username, 'password': password})
