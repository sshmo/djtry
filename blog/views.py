"""Views module."""

from django.shortcuts import render

# Create your views here.


def post_list(request):
    """Renders post list from templates."""
    return render(request, "blog/post_list.html", {})
