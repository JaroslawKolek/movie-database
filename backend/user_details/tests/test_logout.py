from django.shortcuts import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from user_details.utils import create_test_user_and_user_details


class UserLogoutTestCase(APITestCase):
    """ Test User logout endpoint """

    def test_permissions(self):
        response = self._logout()
        self.assertEqual(response.status_code, 401)

    def test_logout_user_when_user_has_login_token(self):
        user, _ = create_test_user_and_user_details('username_has_token', 'password')
        self.client.force_authenticate(user)
        Token.objects.create(user=user)
        response = self._logout()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user=user).count(), 0)

    def test_logout_user_when_user_has_no_login_token(self):
        user, _ = create_test_user_and_user_details('username_has_no_token', 'password')
        self.client.force_authenticate(user)
        self.assertEqual(Token.objects.filter(user=user).count(), 0)
        response = self._logout()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user=user).count(), 0)

    def _logout(self):
        url = reverse('user_details:logout')
        return self.client.post(url)
