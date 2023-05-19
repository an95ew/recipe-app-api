"""
Test for models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email(self):
        """Test creating a user with email and password successful."""
        email = "test@example.com"
        password = "123123123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, '123123')
            self.assertEqual(user.email, expected)

    def test_create_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a Value Error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '123')

    def test_create_superuser(self):
        """Test if creating of superuser is successful"""
        user = get_user_model().objects.create_superuser('Example@test.com', '123123')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_recipe(self):
        """Test creating a recipe is succesful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'pass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)

