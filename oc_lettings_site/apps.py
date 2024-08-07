"""This module provides app management for the website application.
Classes:
    - OCLettingsSiteConfig: Handles the config of the website app.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """This class defines the configuration for the 'oc_lettings_site' app, including its name.
    Django uses this class to configure application-specific settings.

    Attributes:
        name (str): The name of the application, which Django uses to refer to the app internally.
    """
    name = 'oc_lettings_site'
