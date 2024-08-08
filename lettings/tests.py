"""This module provides tests for the Lettings application."""


from django.test import TestCase
from django.urls import reverse
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
