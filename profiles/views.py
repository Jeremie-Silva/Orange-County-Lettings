"""This module provides views for the Profiles application.
Functions:
    - index(): view for index page.
    - profile(): view for item page.
"""

from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """Render the index page for the Profiles application.
    Args:
        request (HttpRequest): The HTTP request object that contains metadata about the request.
    Returns:
        HttpResponse: The HTTP response object containing the rendered index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis, pellentesque
# dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo
# tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus
# et netus et males
def profile(request, username):
    """Render the profile item page for the Profiles application.
    Args:
        request (HttpRequest): The HTTP request object that contains metadata about the request.
    Returns:
        HttpResponse: The HTTP response object containing the rendered profile item page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
