"""This module provides views for the website application.
Functions:
    - index(): view for index page.
"""

from django.shortcuts import render
from sentry_sdk import capture_exception


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """Render the index page for the website application.
    Args:
        request (HttpRequest): The HTTP request object that contains metadata about the request.
    Returns:
        HttpResponse: The HTTP response object containing the rendered index page.
    """
    try:
        return render(request, 'oc_lettings_site/index.html')
    except Exception as exc:
        capture_exception(exc)
        raise
