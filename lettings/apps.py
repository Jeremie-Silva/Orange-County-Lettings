"""This module provides app management for the Lettings application.
Classes:
    - LettingsConfig: Handles the config of Lettings app.
"""


from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """This class defines the configuration for the 'lettings' app, including its name.
    Django uses this class to configure application-specific settings.

    Attributes:
        name (str): The name of the application, which Django uses to refer to the app internally.
    """
    name = 'lettings'
