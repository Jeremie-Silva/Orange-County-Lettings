"""This module provides tests for the website application."""


from django.test import TestCase
from django.urls import reverse


class WebsiteAppTests(TestCase):
    """Test suite for the website application."""

    def test_home_page_view(self):
        """This test ensures that the home page is accessible and returns a successful response."""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Holiday Homes")

    def test_404_page(self):
        """This test ensures that the custom 404 page is displayed when a page is not found."""
        response = self.client.get("/non-existent-page/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Resource Not Found", status_code=404)

    def test_500_page(self):
        """This test ensures that the custom 500 page is displayed when there is a server error."""
        with self.assertRaises(Exception):
            response = self.client.get(reverse("error"))
            self.assertEqual(response.status_code, 500)
            self.assertContains(response, "Server Error")
