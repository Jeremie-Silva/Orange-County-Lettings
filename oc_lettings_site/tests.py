"""This module provides tests for the website application."""


from django.test import TestCase
from unittest.mock import patch
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

    @patch("oc_lettings_site.views.render")
    def test_500_page(self, render):
        """This test ensures that the custom 500 page is displayed when there is a server error."""
        render.side_effect = Exception("Simulated exception")
        with self.assertRaises(Exception):
            response = self.client.get(reverse("index"))
            self.assertEqual(response.status_code, 500)
            self.assertContains(response, "Server Error")

    @patch("oc_lettings_site.views.capture_exception")
    @patch("oc_lettings_site.views.render")
    def test_home_page_view_sentry_logs(self, render, sentry):
        """This test forces an exception to be raised in the index view,
        ensuring that the exception handling is given to sentry.
        """
        render.side_effect = Exception("Simulated exception")
        with self.assertRaises(Exception):
            response = self.client.get(reverse("index"))
            self.assertEqual(response.status_code, 500)
        sentry.assert_called_once()
