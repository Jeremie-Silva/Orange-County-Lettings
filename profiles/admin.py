"""This module provides admin for the Profiles application."""

from django.contrib import admin
from .models import Profile


admin.site.register(Profile)
