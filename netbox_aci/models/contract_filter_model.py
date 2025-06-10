"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from netbox.models import NetBoxModel
from .. choices import ContractFilterDirectivesChoices, ContractFilterACtionChoices
from . contract_subject_model import ContractSubject

__all__ = (
    "ContractFilter",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class ContractFilter(NetBoxModel):
    """
    This class definition defines a Django model for a contract filter.
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

    contractsubject = models.ForeignKey(
        ContractSubject,
        on_delete=models.CASCADE,
        related_name="filter_subject",
        blank=True,
        null=True,
    )

    directives = models.CharField(
        choices=ContractFilterDirectivesChoices,
        blank=True,
    )

    action = models.CharField(
        choices=ContractFilterACtionChoices,
        blank=True,
    )

    #Metadata
    class Meta:
        ordering = ["name"]
        verbose_name = "Contract Filter"
        verbose_name_plural = "Contract Filters"
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'contractsubject'],
                name='unique_filter_per_contractsubject'
            ),
            models.UniqueConstraint(
                fields=['slug', 'contractsubject'],
                name='unique_slug_per_contractsubject'
            ),
        ]

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:contractfilter', args=[self.pk])
