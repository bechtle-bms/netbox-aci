"""
Define the django form elements for the user interface. 
"""

from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms import get_field_value
from utilities.forms.fields import SlugField
from utilities.forms.rendering import FieldSet
from .. models import contract_filter_entry_model

__all__ = (
    "ContractFilterEntryForm",
)


class ContractFilterEntryForm(NetBoxModelForm):

    slug = SlugField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'contractfilter',
            'ether_type',
            'ip_protocol',
            'arp_flag',
            'sport_from',
            'sport_to',
            'dport_from',
            'dport_to',
        ),
    )

    class Meta:
        model = contract_filter_entry_model.ContractFilterEntry

        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'contractfilter',
            'ether_type',
            'ip_protocol',
            'arp_flag',
            'sport_from',
            'sport_to',
            'dport_from',
            'dport_to',            
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ether_type = get_field_value(self, 'ether_type')

        if ether_type:

            # Remove ARP flag for ip protocols.
            if ether_type in ['ip', 'ipv4', 'ipv6']:
                self.fields.pop('arp_flag', None)
                self.fields['ether_type'] = forms.ChoiceField(
                    choices=[(ether_type, ether_type)],
                    required=False
                )

            # Remove many input fields for protocols like trill, etc.
            elif ether_type in ['mpls_unicast', 'unspecified', 'trill', 'fcoe', 'mac_security']:
                for field in ['arp_flag', 'ip_protocol', 'sport_from', 'sport_to', 'dport_from', 'dport_to']:
                    self.fields.pop(field, None)
                self.fields['ether_type'] = forms.ChoiceField(
                    choices=[(ether_type, ether_type)],
                    required=False
                )

            # Remove IP-related fields from ARP.
            elif ether_type == 'arp':
                for field in ['ip_protocol', 'sport_from', 'sport_to', 'dport_from', 'dport_to']:
                    self.fields.pop(field, None)
                self.fields['ether_type'] = forms.ChoiceField(
                    choices=[("arp", "arp")],
                    required=False
                )

    def clean(self):
        super().clean()

        ip_protocol = self.cleaned_data.get("ip_protocol")
        sport_from = self.cleaned_data.get("sport_from")
        sport_to = self.cleaned_data.get("sport_to")
        dport_from = self.cleaned_data.get("dport_from")
        dport_to = self.cleaned_data.get("dport_to")

        no_port_protocols = {
            'egp', 'eigrp', 'icmp', 'icmpv6', 'igmp', 'igp', 'l2tp', 'ospf', 'pim', 'unspecified'
        }

        if ip_protocol and ip_protocol in no_port_protocols:
            if sport_from or sport_to or dport_from or dport_to:
                self.add_error(None, f"Protocol '{ip_protocol}' does not support port numbers.")
