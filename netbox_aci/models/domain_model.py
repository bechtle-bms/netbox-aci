"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import DomainTypeChoices, PoolAllocationModeChoices
from . default_model import ACIDefault

__all__ = (
    "Domain",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class Domain(ACIDefault):
    """
    This class definition defines a Django model for Physical and External Domains.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    domain_type = models.CharField(
        choices=DomainTypeChoices,
        blank=True,
    )

    vlan_pool = models.ForeignKey(
        on_delete=models.PROTECT,
        to='ipam.VLANGroup',
    )

    pool_allocation_mode = models.CharField(
        choices=PoolAllocationModeChoices,
        blank=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Domain"
        verbose_name_plural = "Domains"

    #Metadata
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:domain', args=[self.pk])
