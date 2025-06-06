"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from ..choices import LinkLevelNegotiationChoices, LinkLevelSpeedChoices, GenericDisabledEnabledChoices, PortChannelChoices
from .default_model import ACIDefault

__all__ = (
    "LinkLevel",
    "CDP",
    "LLDP",
    "PortChannel"
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


class CDP(ACIDefault):
    """
    This class definition defines a Django model for an Interface CDP Policy.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    admin_state = models.CharField(
        choices=GenericDisabledEnabledChoices,
        default='disabled',
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "CDP Policy"
        verbose_name_plural = "CDP Policies"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:cdp', args=[self.pk])


class LLDP(ACIDefault):
    """
    This class definition defines a Django model for an Interface LLDP Policy.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    receive_state = models.CharField(
        choices=GenericDisabledEnabledChoices,
        default='disabled',
    )

    transmit_state = models.CharField(
        choices=GenericDisabledEnabledChoices,
        default='disabled',
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "LLDP Policy"
        verbose_name_plural = "LLDP Policies"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:lldp', args=[self.pk])


class PortChannel(ACIDefault):
    """
    This class definition defines a Django model for an Interface PortChannel Policy.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    mode = models.CharField(
        choices=PortChannelChoices,
        default='staticchannel',
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "PortChannel Policy"
        verbose_name_plural = "PortChannel Policies"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:portchannel', args=[self.pk])
