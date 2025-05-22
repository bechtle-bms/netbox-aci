"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import LinkLevelNegotiationChoices, LinkLevelSpeedChoices
from . default_model import ACIDefault

__all__ = (
    "LinkLevel",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class LinkLevel(ACIDefault):
    """
    This class definition defines a Django model for an Interface LinkLevel Policy.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    negotiation = models.CharField(
        choices=LinkLevelNegotiationChoices,
        blank=True,
    )

    speed = models.CharField(
        choices=LinkLevelSpeedChoices,
        blank=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Link Level Policy"
        verbose_name_plural = "Link Level Policies"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:linklevel', args=[self.pk])
