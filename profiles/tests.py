"""This module provides tests for the Profiles application."""


from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth.models import User
from .models import Profile


class ProfilesTests(TestCase):
    """Test suite for the Profiles application endpoints."""

    def setUp(self):
        """Set up test data for the Profiles application. This method creates a fake user and
        a fake profile that will be used in the tests for the Profiles application's endpoints.
        """
        self.user = User.objects.create_user(
            username="test user",
            password="12345",
            email="test@email.fr",
            first_name="first name test",
            last_name="last name test",
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="test city"
        )

    def test_profile_list_view(self):
        """This test ensures that the profile list view is accessible and returns a
        successful response.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test user")

    @patch("profiles.views.capture_exception")
    @patch("profiles.views.Profile.objects.all")
    def test_profile_list_view_sentry_logs(self, mock_all, sentry):
        """This test forces an exception to be raised in the profile list view,
        ensuring that the exception handling is given to sentry.
        """
        mock_all.side_effect = Exception("Simulated exception")
        with self.assertRaises(Exception):
            response = self.client.get(reverse("profiles:index"))
            self.assertEqual(response.status_code, 500)
        sentry.assert_called_once()

    def test_profile_detail_view(self):
        """This test ensures that the profile detail view is accessible, returns a
        successful response, and displays the correct profile details.
        """
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test user")
        self.assertContains(response, "test city")
        self.assertContains(response, "test@email.fr")
        self.assertContains(response, "first name test")
        self.assertContains(response, "last name test")

    @patch("profiles.views.capture_exception")
    @patch("profiles.views.Profile.objects.get")
    def test_profile_detail_view_sentry_logs(self, mock_get, sentry):
        """This test forces an exception to be raised in the profile detail view,
        ensuring that the exception handling is given to sentry.
        """
        mock_get.side_effect = Exception("Simulated exception")
        with self.assertRaises(Exception):
            response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
            self.assertEqual(response.status_code, 500)
        sentry.assert_called_once()
