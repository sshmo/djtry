"""Models for blog app."""

from django.conf import settings
from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, TextField
from django.utils import timezone


class Post(models.Model):
    """Post class.

    Attributes:
        author: author of the post.
        title: title of the post.
        text: post content.
        created_date: date of post creation.
        published_date: date of post publication.
    """

    author: ForeignKey = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title: CharField = models.CharField(max_length=200)
    text: TextField = models.TextField()
    created_date: DateTimeField = models.DateTimeField(default=timezone.now)
    published_date: DateTimeField = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Add published_date to post."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Post representation."""
        return self.title
