"""
Define django models
"""

from netbox.models import NetBoxModel
from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import AAEPStaticBindingModeChoices
from . default_model import ACIDefault
from . import domain_model, ap_model, epg_model

__all__ = (
    "AAEP",
    "AAEPStaticBinding",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)

vid_validation = RegexValidator(
    r"^vlan-(?:[1-9][0-9]{0,2}|[1-3][0-9]{3}|40[0-3][0-9]|409[0-4])$",
    "Vlan must be in the form vlan-[1-4094]",
)


class AAEP(ACIDefault):
    """
    This class definition defines a Django model for an Attachable Access Entity Profile.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    infrastructure_vlan = models.BooleanField(
        default=False,
    )

    domains = models.ManyToManyField(
        domain_model.Domain,
        related_name = "aaep_domain",
        blank=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "AAEP"
        verbose_name_plural = "AAEPs"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:aaep', args=[self.pk])


class AAEPStaticBinding(NetBoxModel):
    """
    This class definition defines a Django model for an Static Binding in anAttachable Access Entity Profile.
    """
    aaep = models.ForeignKey(
        AAEP,
        on_delete=models.CASCADE,
        related_name="aaepstaticbinding_aaep",
    )

    index = models.PositiveIntegerField(
        null=True
    )

    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.CASCADE,
        related_name="aaepstaticbinding_tenant",
        null=True,
    )

    applicationprofile = models.ForeignKey(
        ap_model.ApplicationProfile,
        on_delete=models.CASCADE,
        related_name="aaepstaticbinding_applicationprofile",
        null=True,
    )

    epg = models.ForeignKey(
        epg_model.EndPointGroup,
        on_delete=models.CASCADE,
        related_name="aaepstaticbinding_epg",
        null=True,
    )

    encap = models.CharField(
        max_length=9,
        validators=[vid_validation],
        null=True,
        help_text=("Prefix vlan- followed by a numeric VLAN ID (1-4094)")
    )

    mode = models.CharField(
        choices=AAEPStaticBindingModeChoices,
    )

    #Metadata
    class Meta:
        ordering = ["aaep", "index"]
        unique_together = ["aaep", "index"]

    #Methods
    def __str__(self):
        return self.aaep.slug

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:aaepstaticbinding', args=[self.pk])
