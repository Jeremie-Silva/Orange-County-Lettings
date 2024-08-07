"""This module provides admin for the Lettings application."""

from django.contrib import admin
from .models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)
