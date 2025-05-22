"""
Define the django form elements for the user interface. 
"""

from django import forms
from ipam.models import IPAddress, VRF
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from .. models import bd_model, l3out_model


class BridgeDomainForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    subnets = forms.ModelMultipleChoiceField(
        queryset=IPAddress.objects.filter(custom_field_data={"gateway": True}),
        required=False
    )

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',            
            'vrf',
            'l2_unknown_unicast',
            'arp_flooding',
            'unicast_routing',
            'subnets',
            'l3outs',
        ),
    )

    class Meta:
        model = bd_model.BridgeDomain

        fields = (
            'name',
            'slug',
            'description',            
            'comments',
            'vrf',
            'l2_unknown_unicast',
            'arp_flooding',
            'unicast_routing',
            'subnets',
            'l3outs',
        )


class BridgeDomainFilterForm(NetBoxModelFilterSetForm):

    model = bd_model.BridgeDomain

    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        required=False
    )

    l3outs = forms.ModelMultipleChoiceField(
        queryset=l3out_model.L3Out.objects.all(),
        required=False
    )
