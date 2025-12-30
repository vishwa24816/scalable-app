from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        
        # Set default role if not provided
        if 'role' not in extra_fields:
            user.role = 'GENERAL_USER'
            
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.role = 'SYSTEM_ADMINISTRATOR'
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    ROLE_CHOICES = (
        ('GENERAL_USER', 'General User'),
        ('TEAM_MEMBER', 'Team Member'),
        ('SYSTEM_ADMINISTRATOR', 'System Administrator'),
    )

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='GENERAL_USER'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'