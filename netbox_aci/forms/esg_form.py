"""
Define the django form elements for the user interface. 
"""

from django import forms
from ipam.models import VRF, Prefix
from extras.models import Tag
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet, TabbedGroups
from .. models import esg_model, ap_model, contract_model, epg_model


class EndPointSecurityGroupForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            TabbedGroups(
                FieldSet(
                    'name',
                    'slug',
                    'description',
                    'applicationprofile',
                    'vrf',
                    'contracts_consume',
                    'contracts_provide',
                    name = "ESG",
                ),
                FieldSet(
                    'epgs_selector',
                    'ip_subnets_selector',
                    'tags_selector',
                    name = "Selectors"
                ),
            ),
        ),
    )

    class Meta:
        model = esg_model.EndPointSecurityGroup
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'applicationprofile',
            'vrf',
            'contracts_consume',
            'contracts_provide',
            'epgs_selector',
            'ip_subnets_selector',
            'tags_selector',
        )


class EndPointSecurityGroupFilterForm(NetBoxModelFilterSetForm):

    model = esg_model.EndPointSecurityGroup

    applicationprofile = DynamicModelChoiceField(
        queryset=ap_model.ApplicationProfile.objects.all(),
        required=False
    )

    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
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

    epgs_selector = forms.ModelMultipleChoiceField(
        queryset=epg_model.EndPointGroup.objects.all(),
        required=False
    )

    ip_subnets_selector = forms.ModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )

    tags_selector = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False
    )
