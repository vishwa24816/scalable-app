from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from users.permissions import IsSystemAdmin, IsTeamMember

User = get_user_model()

class PermissionsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='password123'
        )
        self.team_user = User.objects.create_user(
            email='team@example.com',
            password='password123',
            role='TEAM_MEMBER'
        )
        self.general_user = User.objects.create_user(
            email='user@example.com',
            password='password123',
            role='GENERAL_USER'
        )

    def test_is_system_admin_permission(self):
        """
        Test that only SYSTEM_ADMINISTRATOR has IsSystemAdmin permission.
        """
        permission = IsSystemAdmin()
        
        request_admin = self.factory.get('/')
        request_admin.user = self.admin_user
        self.assertTrue(permission.has_permission(request_admin, None))
        
        request_team = self.factory.get('/')
        request_team.user = self.team_user
        self.assertFalse(permission.has_permission(request_team, None))

    def test_is_team_member_permission(self):
        """
        Test that TEAM_MEMBER or above has permission.
        """
        permission = IsTeamMember()
        
        request_team = self.factory.get('/')
        request_team.user = self.team_user
        self.assertTrue(permission.has_permission(request_team, None))
        
        request_admin = self.factory.get('/')
        request_admin.user = self.admin_user
        self.assertTrue(permission.has_permission(request_admin, None))
        
        request_user = self.factory.get('/')
        request_user.user = self.general_user
        self.assertFalse(permission.has_permission(request_user, None))
