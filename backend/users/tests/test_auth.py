from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

TOKEN_OBTAIN_URL = reverse('users:token_obtain_pair')
TOKEN_REFRESH_URL = reverse('users:token_refresh')

class AuthApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.email = 'test@example.com'
        self.password = 'password123'
        self.user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
            name='Test User'
        )

    def test_login_successful(self):
        """
        Test that a user can login and receive JWT tokens.
        """
        payload = {'email': self.email, 'password': self.password}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)

    def test_login_invalid_credentials(self):
        """
        Test that login fails with invalid credentials.
        """
        payload = {'email': self.email, 'password': 'wrongpassword'}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_refresh(self):
        """
        Test that a refresh token can be used to get a new access token.
        """
        payload = {'email': self.email, 'password': self.password}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)
        refresh_token = res.data['refresh']
        
        payload_refresh = {'refresh': refresh_token}
        res_refresh = self.client.post(TOKEN_REFRESH_URL, payload_refresh)
        
        self.assertEqual(res_refresh.status_code, status.HTTP_200_OK)
        self.assertIn('access', res_refresh.data)

    def test_logout_successful(self):
        """
        Test that a user can logout by blacklisting their refresh token.
        """
        payload = {'email': self.email, 'password': self.password}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)
        access_token = res.data['access']
        refresh_token = res.data['refresh']
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        logout_url = reverse('users:logout')
        res_logout = self.client.post(logout_url, {'refresh': refresh_token})
        
        self.assertEqual(res_logout.status_code, status.HTTP_205_RESET_CONTENT)

    def test_logout_invalid_token(self):
        """
        Test that logout fails with an invalid token.
        """
        payload = {'email': self.email, 'password': self.password}
        res = self.client.post(TOKEN_OBTAIN_URL, payload)
        access_token = res.data['access']
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        logout_url = reverse('users:logout')
        res_logout = self.client.post(logout_url, {'refresh': 'invalidtoken'})
        self.assertEqual(res_logout.status_code, status.HTTP_400_BAD_REQUEST)
