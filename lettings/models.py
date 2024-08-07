"""This module provides models for the Lettings application.
Classes:
    - Address: Model for addresses data.
    - Letting: Model for lettings data.
"""


from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Model representing an address.

    The Address model stores detailed information about an address. It is used to associate
    specific address information with lettings or other entities within the Lettings application.

    Attributes:
        number (int): The street number for the address,
            validated to be a positive integer and cannot exceed 9999.
        street (str): The street name, limited to 64 characters.
        city (str): The city name, limited to 64 characters.
        state (str): The state code, which must be exactly 2 characters long.
        zip_code (int): The postal code, validated to be a positive integer
            and cannot exceed 99999.
        country_iso_code (str): The ISO code for the country,
            which must be exactly 3 characters long.

    Methods:
        __str__(): Returns a string representation of the address, with number and street.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Returns a string representation of the address, with number and street."""
        return f'{self.number} {self.street}'

    class Meta:
        """Meta options for the Address model.

        The Meta class contains configuration options that apply to the Address model.
        It is used to specify the verbose names for the model, both singular and plural.

        Attributes:
            verbose_name (str): A human-readable name for the model, used in singular form.
            verbose_name_plural (str): A human-readable name for the model, used in plural form.
        """
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """Model representing a letting.

    The Letting model stores information about a specific letting, each letting is linked
    to a single address, forming a one-to-one relationship between Letting and Address.

    Attributes:
        title (str): The title of the letting, typically used to identify the letting in listings.
        address (Address): A one-to-one relationship with the Address model,
            representing the physical location of the letting.

    Methods:
        __str__(): Returns a string representation of the letting, with title.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of the letting, with title."""
        return self.title
