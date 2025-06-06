"""
Define the django form elements for the user interface. 
"""

from django import forms
from dcim.models import Device, Interface
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from .. models import ipg_model, aaep_model

__all__ = (
    "PolicyGroupForm",
    "PolicyGroupAssignementForm",
    "PolicyGroupFilterForm",
)


class PolicyGroupForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'type',
            'aaep',
            'linklevel',
            'cdp',
            'lldp',
            'portchannel',
        ),
    )

    class Meta:
        model = ipg_model.PolicyGroup
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'type',
            'aaep',
            'linklevel',
            'cdp',
            'lldp',
            'portchannel',
        )

    def clean(self):
        """
        Validate input combination
        """
        super().clean()

        ipg_type = self.cleaned_data.get("type")
        portchannel = self.cleaned_data.get("portchannel")

        if ipg_type == "access" and portchannel is not None:
            raise forms.ValidationError("Access type cannot have portchannel enabled")
        if ipg_type != "access" and portchannel is None:
            raise forms.ValidationError("Non-access type must have portchannel enabled")


class PolicyGroupAssignementForm(NetBoxModelForm):

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        required=False,
        query_params={
            "device_id": "$device",
        },
    )

    fieldsets = (
        FieldSet(
            'ipg',
            'device',
            'interface',
        ),
    )

    class Meta:
        model = ipg_model.PolicyGroupAssignement
        fields = (
            'ipg',
            'device',
            'interface',
        )

    def clean(self):
        """
        Prevent duplicate entries
        """
        super().clean()

        ipg = self.cleaned_data.get("ipg")
        device = self.cleaned_data.get("device")
        interface = self.cleaned_data.get("interface")

        if ipg and device and interface:
            if ipg_model.PolicyGroupAssignement.objects.filter(
                ipg=ipg,
                device=device,
                interface=interface
            ).exists():
                self.add_error("interface", "Duplicate entry")


class PolicyGroupFilterForm(NetBoxModelFilterSetForm):

    model = ipg_model.PolicyGroup

    aaep = DynamicModelChoiceField(
        queryset=aaep_model.AAEP.objects.all(),
        required=False
    )
