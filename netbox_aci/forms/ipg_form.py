"""
Define the django form elements for the user interface. 
"""

from dcim.models import Device, Interface
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from .. models import ipg_model, aaep_model


class PolicyGroupForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'aaep',
            'linklevel',
        ),
    )

    class Meta:
        model = ipg_model.PolicyGroup
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'aaep',
            'linklevel',
        )


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
            if ipg_model.PolicyGroupAssignement.objects.filter(ipg=ipg, device=device, interface=interface).exists():
                self.add_error("interface", "Duplicate entry")


class PolicyGroupFilterForm(NetBoxModelFilterSetForm):

    model = ipg_model.PolicyGroup

    aaep = DynamicModelChoiceField(
        queryset=aaep_model.AAEP.objects.all(),
        required=False
    )
