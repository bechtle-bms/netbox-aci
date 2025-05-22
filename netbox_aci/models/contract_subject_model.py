"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import ContractQoSClassChoices, ContractTargetDSCPChoices
from . default_model import ACIDefault
from . contract_model import Contract

__all__ = (
    "ContractSubject",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class ContractSubject(ACIDefault):
    """
    This class definition defines a Django model for a contract subject.
    """    
    name = models.CharField(
        verbose_name=('name'),
        max_length=50,
        unique=True,
        validators=[input_validation],
    )

    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name="subject_contract",
        blank=True,
        null=True,
    )

    target_dscp = models.CharField(
        choices=ContractTargetDSCPChoices,
        blank=True,
    )

    qos_priority = models.CharField(
        choices=ContractQoSClassChoices,
        blank=True,
    )

    apply_both_directions = models.BooleanField(
        default=True,
    )

    reverse_filter_ports = models.BooleanField(
        default=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Contract Subject"
        verbose_name_plural = "Contract Subjects"

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:contractsubject', args=[self.pk])
