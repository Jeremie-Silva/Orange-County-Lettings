"""This module provides models for the Profiles application.
Classes:
    - Profile: Model for profiles data.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a user profile.

    The Profile model is linked to a Django User model via a one-to-one relationship.
    It is used to store additional information about a user, specifically their favorite city.

    Attributes:
        user (User): A one-to-one relationship with the Django User model.
            This field links the Profile to a specific user account.
        favorite_city (str): A string field for storing the user's favorite city.
            This field is optional and can be left blank.

    Methods:
        __str__(): Returns a string representation of the profile, with username.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Returns a string representation of the profile, with username."""
        return self.user.username
