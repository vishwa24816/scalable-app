from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('users:create')

class UserApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_successful(self):
        """
        Test creating a user via the API is successful.
        """
        payload = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'name': 'Test User'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(user.name, payload['name'])

    def test_create_user_invalid_data(self):
        """
        Test creating a user with invalid data fails.
        """
        payload = {
            'email': '',
            'password': 'testpassword123',
            'name': 'Test User'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
