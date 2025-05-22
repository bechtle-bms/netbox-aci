"""
Define django models
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from . default_model import ACIDefault
from . import ap_model, contract_model, epg_model

__all__ = (
    "EndPointSecurityGroup",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class EndPointSecurityGroup(ACIDefault):
    """
    This class definition defines a Django model for an EndPointSecurityGroup.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    applicationprofile = models.ForeignKey(
        ap_model.ApplicationProfile,
        on_delete=models.PROTECT,
        null=True,
    )

    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    contracts_consume = models.ManyToManyField(
        contract_model.Contract,
        related_name = "esg_contract_consume",
        blank=True,
    )

    contracts_provide = models.ManyToManyField(
        contract_model.Contract,
        related_name="esg_contract_provide",
        blank=True,
    )

    epgs_selector = models.ManyToManyField(
        epg_model.EndPointGroup,
        related_name="esg_epg_selector",
        blank=True,
    )

    ip_subnets_selector = models.ManyToManyField(
        to='ipam.Prefix',
        related_name = "esg_ip_subnet_selector",
        blank=True,
    )

    tags_selector = models.ManyToManyField(
        to='extras.Tag',
        related_name = "esg_tag_selector",
        blank=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "End Point Security Group"
        verbose_name_plural = "End Point Security Groups"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:endpointsecuritygroup', args=[self.pk])
