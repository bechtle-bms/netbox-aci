"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import ContractScopeChoices, ContractQoSClassChoices, ContractTargetDSCPChoices
from . default_model import ACIDefault

__all__ = (
    "Contract",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class Contract(ACIDefault):
    """
    This class definition defines a Django model for a contract.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    scope = models.CharField(
        choices=ContractScopeChoices,
        blank=True,
    )

    qos_class = models.CharField(
        choices=ContractQoSClassChoices,
        blank=True,
    )

    target_dscp = models.CharField(
        choices=ContractTargetDSCPChoices,
        blank=True,
    )

    vrfs_consume = models.ManyToManyField(
        to='ipam.VRF',
        related_name = "vrf_contract_consume",
        blank=True,
    )

    vrfs_provide = models.ManyToManyField(
        to='ipam.VRF',
        related_name = "vrf_contract_provide",
        blank=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:contract', args=[self.pk])
