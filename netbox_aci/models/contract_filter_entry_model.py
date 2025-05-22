"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import ContractFilterEntryEtherTypeChoices, ContractFilterEntryIPProtocolChoices, ContractFilterEntryARPFlagChoices
from . default_model import ACIDefault
from . contract_filter_model import ContractFilter

__all__ = (
    "ContractFilterEntry",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)

port_validation = RegexValidator(
    r"^(1|6[0-5][0-5][0-3][0-5]|[1-5][0-9][0-9][0-9][0-9]|[1-9][0-9]{0,3})$",
    "Port must be in the form 1-65535"
)


class ContractFilterEntry(ACIDefault):
    """
    This class definition defines a Django model for an entry within a contract filter.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=50,
        unique=True,
        validators=[input_validation],
    )

    contractfilter = models.ForeignKey(
        ContractFilter,
        on_delete=models.CASCADE,
        related_name="entry_filter",
        blank=True,
        null=True,
    )

    ether_type = models.CharField(
        choices=ContractFilterEntryEtherTypeChoices,
        blank=True,
    )

    ip_protocol = models.CharField(
        choices=ContractFilterEntryIPProtocolChoices,
        blank=True,
    )

    arp_flag = models.CharField(
        choices=ContractFilterEntryARPFlagChoices,
        blank=True,
    )

    sport_from = models.CharField(
        max_length=5,
        validators=[port_validation],
        blank=True,
        null=True,
        help_text=("source port 1-65535")
    )

    sport_to = models.CharField(
        max_length=5,
        validators=[port_validation],
        blank=True,
        null=True,
        help_text=("source port 1-65535")
    )

    dport_from = models.CharField(
        max_length=5,
        validators=[port_validation],
        blank=True,
        null=True,
        help_text=("destination port 1-65535")
    )

    dport_to = models.CharField(
        max_length=5,
        validators=[port_validation],
        blank=True,
        null=True,
        help_text=("destination port 1-65535")
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Contract Filter Entry"
        verbose_name_plural = "Contract Filter Entries"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:contractfilterentry', args=[self.pk])
