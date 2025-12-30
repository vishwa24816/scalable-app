from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful.
        """
        email = 'test@example.com'
        password = 'testpassword123'
        user = User.objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.role, 'GENERAL_USER') # Default role

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized.
        """
        email = 'test@EXAMPLE.COM'
        user = User.objects.create_user(email, 'testpassword123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating a user with no email raises an error.
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'testpassword123')

    def test_create_superuser(self):
        """
        Test creating a new superuser.
        """
        user = User.objects.create_superuser(
            'test@example.com',
            'testpassword123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.role, 'SYSTEM_ADMINISTRATOR')

    def test_user_roles(self):
        """
        Test that user roles are correctly assigned.
        """
        user = User.objects.create_user('user@example.com', 'pass123', role='TEAM_MEMBER')
        self.assertEqual(user.role, 'TEAM_MEMBER')
