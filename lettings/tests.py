"""This module provides tests for the Lettings application."""


from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import Address, Letting


class LettingsTests(TestCase):
    """Test suite for the Lettings application endpoints."""

    def setUp(self):
        """Set up test data for the Lettings application. This method creates fake address
        and fake letting that will be used in the tests for the Lettings application's endpoints.
        """
        self.address = Address.objects.create(
            number=123,
            street="Fake Street",
            city="Faketown",
            state="FR",
            zip_code=12345,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_letting_list_view(self):
        """This test ensures that the letting list view is accessible and returns a
        successful response.
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    @patch("lettings.views.capture_exception")
    @patch("lettings.views.Letting.objects.all")
    def test_letting_list_view_sentry_logs(self, mock_all, sentry):
        """This test forces an exception to be raised in the letting list view,
        ensuring that the exception handling is given to sentry.
        """
        mock_all.side_effect = Exception("Simulated exception")
        with self.assertRaises(Exception):
            response = self.client.get(reverse("lettings:index"))
            self.assertEqual(response.status_code, 500)
        sentry.assert_called_once()

    def test_letting_detail_view(self):
        """This test ensures that the letting detail view is accessible, returns a
        successful response, and displays the correct letting details.
        """
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "Fake Street")
        self.assertContains(response, "Faketown")
        self.assertContains(response, "123")
        self.assertContains(response, "12345")
        self.assertContains(response, "FRA")

    @patch("lettings.views.capture_exception")
    @patch("lettings.views.Letting.objects.get")
    def test_letting_detail_view_sentry_logs(self,  mock_get, sentry):
        """This test forces an exception to be raised in the letting detail view,
        ensuring that the exception handling is given to sentry.
        """
        mock_get.side_effect = Exception("Simulated exception")
        with self.assertRaises(Exception):
            response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
            self.assertEqual(response.status_code, 500)
        sentry.assert_called_once()
