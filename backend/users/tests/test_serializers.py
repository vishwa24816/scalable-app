from django.test import TestCase
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

User = get_user_model()

class UserSerializerTest(TestCase):
    def test_user_serializer_valid_data(self):
        """
        Test that the serializer creates a user with valid data.
        """
        payload = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'name': 'Test User'
        }
        serializer = UserSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        
        self.assertEqual(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(user.name, payload['name'])
        self.assertNotIn('password', serializer.data)

    def test_user_serializer_invalid_email(self):
        """
        Test that the serializer fails with an invalid email.
        """
        payload = {
            'email': 'invalid-email',
            'password': 'testpassword123',
            'name': 'Test User'
        }
        serializer = UserSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_user_serializer_password_too_short(self):
        """
        Test that the serializer fails if the password is too short.
        """
        payload = {
            'email': 'test@example.com',
            'password': '123',
            'name': 'Test User'
        }
        serializer = UserSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)

    def test_user_serializer_update(self):
        """
        Test updating a user via the serializer.
        """
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='oldpassword123',
            name='Old Name'
        )
        payload = {
            'name': 'New Name',
            'password': 'newpassword123'
        }
        serializer = UserSerializer(instance=user, data=payload, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        
        self.assertEqual(updated_user.name, payload['name'])
        self.assertTrue(updated_user.check_password(payload['password']))
