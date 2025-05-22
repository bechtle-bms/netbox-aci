"""
Define the django form elements for the user interface. 
"""

from django import forms
from django.db.models import Q
from ipam.models import IPAddress
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from .. models import ap_model, epg_model, domain_model, contract_model


class EndPointGroupForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    domains = forms.ModelMultipleChoiceField(
        queryset=domain_model.Domain.objects.filter(
            Q(domain_type='vmm') |
            Q(domain_type='physical')
        )
    )

    subnets = forms.ModelMultipleChoiceField(
        queryset=IPAddress.objects.filter(custom_field_data={"gateway": True}),
        required=False
    )

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'applicationprofile',
            'domains',
            'contracts_consume',
            'contracts_provide',
            'bridgedomain',
            'subnets',
        ),
    )

    class Meta:
        model = epg_model.EndPointGroup
        fields = (
            'name',
            'slug',
            'description',
            'comments',            
            'applicationprofile',
            'domains',
            'contracts_consume',
            'contracts_provide',
            'bridgedomain',
            'subnets',
        )


class EndPointGroupFilterForm(NetBoxModelFilterSetForm):

    model = epg_model.EndPointGroup

    applicationprofile = DynamicModelChoiceField(
        queryset=ap_model.ApplicationProfile.objects.all(),
        required=False
    )

    domains = forms.ModelMultipleChoiceField(
        queryset=domain_model.Domain.objects.all(),
        required=False
    )

    contracts_consume = forms.ModelMultipleChoiceField(
        queryset=contract_model.Contract.objects.all(),
        required=False
    )

    contracts_provide = forms.ModelMultipleChoiceField(
        queryset=contract_model.Contract.objects.all(),
        required=False
    )
