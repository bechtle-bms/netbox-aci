"""
Define django models
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from . default_model import ACIDefault
from . domain_model import Domain

__all__ = (
    "L3Out",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class L3Out(ACIDefault):
    """
    This class definition defines a Django model for an L3Out.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    domains = models.ManyToManyField(
        Domain,
        related_name = "l3out_domain",
        blank=True,
    )

    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )


    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "L3 Out"
        verbose_name_plural = "L3 Outs"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:l3out', args=[self.pk])
