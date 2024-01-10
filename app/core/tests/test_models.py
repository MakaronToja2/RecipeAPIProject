"""
TEST FOR MODELS
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test iof creating user with email was a success"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.password_password(password))