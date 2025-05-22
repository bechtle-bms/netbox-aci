"""
Define the django model.
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from .. choices import ContractFilterDirectivesChoices, ContractFilterACtionChoices
from . default_model import ACIDefault
from . contract_subject_model import ContractSubject

__all__ = (
    "ContractFilter",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class ContractFilter(ACIDefault):
    """
    This class definition defines a Django model for a contract filter.
    """
    name = models.CharField(
        verbose_name=('name'),
        max_length=50,
        unique=True,
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

    #Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_aci:contractfilter', args=[self.pk])
