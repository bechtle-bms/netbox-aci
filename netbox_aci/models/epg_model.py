"""
Define django models
"""

from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from . default_model import ACIDefault
from . import ap_model, contract_model, bd_model, domain_model

__all__ = (
    "EndPointGroup",
)

input_validation = RegexValidator(
    r"^[a-zA-Z0-9-_]+$",
    "Only alphanumeric, hyphens, and underscores are allowed.",
)


class EndPointGroup(ACIDefault):
    """
    This class definition defines a Django model for an EndPointGroup.
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

    domains = models.ManyToManyField(
        domain_model.Domain,
        related_name = "epg_domain",
        blank=True,
    )

    contracts_consume = models.ManyToManyField(
        contract_model.Contract,
        related_name = "epg_contract_consume",
        blank=True,
    )

    contracts_provide = models.ManyToManyField(
        contract_model.Contract,
        related_name="epg_contract_provide",
        blank=True,
    )

    bridgedomain = models.ForeignKey(
        bd_model.BridgeDomain,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    subnets = models.ManyToManyField(
        to='ipam.IPAddress',
        related_name = "epg_subnet",
        blank=True,
    )


    #Metadata    
    class Meta:
        """
        This class definition is for a Django model's metadata,
        which is specifically for a EndPointGroup model.
        """
        ordering = ["name"]
        verbose_name = "End Point Group"
        verbose_name_plural = "End Point Groups"

    #Methods
    def __str__(self):
        """
        This is a special method in Python classes that returns a string
        representation of an object. In this case, when you try to print
        the object or convert an instance of the class to a string,
        it will return the value of the name attribute.

        For example, if you have a EndPointGroup object with name
        "My EndPointGroup", printing it will output "My EndPointGroup".

        This method is defined in epg_model:EndPointGroup.__stract.__str__

        Returns:
            (str) A string representation of the EndPointGroup instance.
        """
        return self.name

    def get_absolute_url(self):
        """
        This method defines a method named get_absolute_url in a Python class.
        When called, it returns the absolute URL for the current instance
        of the EndPointGroup model of the class.
        The URL is generated using the reverse function, which takes
        the name of a URL pattern and a list of arguments. In this case,
        the URL pattern is 'plugins:netbox_aci:endpointgroup' and the argument
        is [self.pk], which is the primary key of the current instance.

        Returns:
            (str) An absolute URL for the current instance of the EndPointGroup model.
        """
        return reverse('plugins:netbox_aci:endpointgroup', args=[self.pk])
