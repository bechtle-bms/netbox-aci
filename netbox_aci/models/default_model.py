from django.db import models
from netbox.models import NetBoxModel


class ACIDefault(NetBoxModel):
    """
    This class definition defines a Django default model.
    """
    slug = models.SlugField(
        verbose_name=('slug'),
        max_length=100,
        unique=True,
        null=True,
    )

    description = models.CharField(
        max_length=100,
        blank=True,
    )

    comments = models.TextField(
        blank=True
    )

    class Meta:
        abstract = True
