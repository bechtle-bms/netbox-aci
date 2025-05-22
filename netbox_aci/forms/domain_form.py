"""
Define the django form elements for the user interface. 
"""

from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from .. models import domain_model


class DomainForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'domain_type',
            'vlan_pool',
            'pool_allocation_mode',
        ),
    )

    class Meta:
        model = domain_model.Domain

        fields = (
            'name',
            'slug',
            'description',            
            'comments',
            'domain_type',
            'vlan_pool',
            'pool_allocation_mode',
        )
