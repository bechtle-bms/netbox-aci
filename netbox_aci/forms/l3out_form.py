"""
Define the django form elements for the user interface. 
"""

from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from .. models import l3out_model, domain_model


class L3OutForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    domains = forms.ModelMultipleChoiceField(
        queryset=domain_model.Domain.objects.filter(domain_type="l3"),
        required=False
    )

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'vrf',
            'domains',
        ),
    )

    class Meta:
        model = l3out_model.L3Out
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'vrf',
            'domains',
        )
