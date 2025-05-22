"""
Define the django form elements for the user interface. 
"""

from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms import get_field_value
from utilities.forms.fields import SlugField
from utilities.forms.rendering import FieldSet
from .. models import contract_filter_entry_model


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

        if get_field_value(self, 'ether_type'):

            if get_field_value(self, 'ether_type') in 'ip, ipv4, ipv6':
                del self.fields['arp_flag']
                self.fields['ether_type'] = forms.ChoiceField(
                    choices=[(get_field_value(self, 'ether_type'), get_field_value(self, 'ether_type'))],
                    required=False
                )

            if get_field_value(self, 'ether_type') in 'mpls_unicast, unspecified, trill, fcoe, mac_security':
                del self.fields['arp_flag']
                del self.fields['ip_protocol']
                del self.fields['sport_from']
                del self.fields['sport_to']
                del self.fields['dport_from']
                del self.fields['dport_to']
                self.fields['ether_type'] = forms.ChoiceField(
                    choices=[(get_field_value(self, 'ether_type'), get_field_value(self, 'ether_type'))],
                    required=False
                )

            if get_field_value(self, 'ether_type') in 'arp':
                del self.fields['ip_protocol']
                del self.fields['sport_from']
                del self.fields['sport_to']
                del self.fields['dport_from']
                del self.fields['dport_to']
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

        if ip_protocol in 'egp, eigrp, icmp, icmpv6, igmp, igp, l2tp, ospf, pim, unspecified':

            if sport_from or sport_to or dport_from or dport_to:
                self.add_error("sport_from", "Ports needed for TCP/UDP")
                self.add_error("sport_to", "Ports needed for TCP/UDP")
                self.add_error("dport_from", "Ports needed for TCP/UDP")
                self.add_error("dport_to", "Ports needed for TCP/UDP")
