"""
Define django models
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import BridgeDomainL2UUCChoices
from . default_model import ACIDefault
from . l3out_model import L3Out

__all__ = (
    "BridgeDomain",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class BridgeDomain(ACIDefault):
    """
    This class definition defines a Django model for a BridgeDomain.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    l2_unknown_unicast = models.CharField(
        choices=BridgeDomainL2UUCChoices,
        default='hardware_proxy',
        blank=True,
    )

    arp_flooding = models.BooleanField(
        default=True,
    )

    unicast_routing = models.BooleanField(
        default=False,
    )

    subnets = models.ManyToManyField(
        to='ipam.IPAddress',
        related_name = "bd_subnet",
        blank=True,
    )

    l3outs = models.ManyToManyField(
        L3Out,
        related_name = "bd_l3out",
        blank=True,
    )


    #Metadata
    class Meta:
        """
        This class definition is for a Django model's metadata,
        which is specifically for a BridgeDomain model.
        """
        ordering = ["name"]
        verbose_name = "Bridge Domain"
        verbose_name_plural = "Bridge Domains"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:bridgedomain', args=[self.pk])
