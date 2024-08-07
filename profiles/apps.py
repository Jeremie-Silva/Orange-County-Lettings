"""This module provides app management for the Profiles application.
Classes:
    - ProfilesConfig: Handles the config of Profiles app.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """This class defines the configuration for the 'profiles' app, including its name.
    Django uses this class to configure application-specific settings.

    Attributes:
        name (str): The name of the application, which Django uses to refer to the app internally.
    """
    name = 'profiles'
