from django.test import TestCase
from django.conf import settings
import os

class SettingsTest(TestCase):
    def test_secret_key_is_not_default(self):
        """
        Verify that the SECRET_KEY is not the default insecure one.
        """
        default_insecure_key = 'django-insecure-_6pm%q-18q&@8=&d+br@sh#*%au*r99zm91t8=**-a8meop$k+'
        self.assertNotEqual(settings.SECRET_KEY, default_insecure_key)

    def test_cors_settings(self):
        """
        Verify that CORS is configured.
        """
        self.assertIn('corsheaders', settings.INSTALLED_APPS)
        self.assertIn('corsheaders.middleware.CorsMiddleware', settings.MIDDLEWARE)
        # Check if CorsMiddleware is before CommonMiddleware
        cors_index = settings.MIDDLEWARE.index('corsheaders.middleware.CorsMiddleware')
        common_index = settings.MIDDLEWARE.index('django.middleware.common.CommonMiddleware')
        self.assertLess(cors_index, common_index)
