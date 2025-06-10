"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from netbox.models import NetBoxModel
from .. choices import ContractQoSClassChoices, ContractTargetDSCPChoices
from . contract_model import Contract

__all__ = (
    "ContractSubject",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class ContractSubject(NetBoxModel):
    """
    This class definition defines a Django model for a contract subject.
    """
    slug = models.SlugField(
        verbose_name=('slug'),
        max_length=100,
        null=True,
        blank=True,
    )

    description = models.CharField(
        max_length=100,
        blank=True,
    )

    comments = models.TextField(
        blank=True
    )

    name = models.CharField(
        verbose_name=('name'),
        max_length=50,
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
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'contract'],
                name='unique_subject_per_contract'
            ),
            models.UniqueConstraint(
                fields=['slug', 'contract'],
                name='unique_slug_per_contract'
            ),
        ]

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:contractsubject', args=[self.pk])
