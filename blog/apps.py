"""App module."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog configs."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
