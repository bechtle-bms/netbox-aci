"""
Define the django model.
"""

from netbox.models import NetBoxModel
from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from . default_model import ACIDefault
from . import aaep_model, policy_link_level_model

__all__ = (
    "PolicyGroup",
    "PolicyGroupAssignement",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class PolicyGroup(ACIDefault):
    """
    This class definition defines a Django model for an Interface Policy Group.
    """
    #Fields
    name = models.CharField(
        verbose_name=('name'),
        max_length=100,
        unique=True,
        validators=[input_validation],
    )

    aaep = models.ForeignKey(
        aaep_model.AAEP,
        on_delete=models.PROTECT,
        related_name="ipg_aaep",
    )

    linklevel = models.ForeignKey(
        policy_link_level_model.LinkLevel,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="ipg_linklevel",
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Policy Group"
        verbose_name_plural = "Policy Groups"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:policygroup', args=[self.pk])


class PolicyGroupAssignement(NetBoxModel):
    """
    This class definition defines a Django model for an Interface Policy Group.
    """
    #Fields
    ipg = models.ForeignKey(
        on_delete=models.CASCADE,
        to=PolicyGroup,
        verbose_name="Policy Group",
        related_name="ipgassignement",
    )

    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    #Metadata
    class Meta:
        ordering = ["ipg"]
        verbose_name = "Policy Group Assignement"
        verbose_name_plural = "Policy Groups Assignements"

    #Methods
    def __str__(self):
        return self.ipg.slug

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:policygroupassignement', args=[self.pk])
