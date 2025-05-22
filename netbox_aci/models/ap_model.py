"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from . default_model import ACIDefault

__all__ = (
    "ApplicationProfile",
)


input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class ApplicationProfile(ACIDefault):
    """
    This class definition defines a Django model for an ApplicationProfile.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    tenant = models.ForeignKey(
        on_delete=models.PROTECT,
        to='tenancy.Tenant',
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Application Profile"
        verbose_name_plural = "Application Profiles"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:applicationprofile', args=[self.pk])
