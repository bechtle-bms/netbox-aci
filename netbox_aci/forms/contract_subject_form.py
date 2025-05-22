"""
Define the django form elements for the user interface. 
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import SlugField
from utilities.forms.rendering import FieldSet
from .. models import contract_subject_model


class ContractSubjectForm(NetBoxModelForm):

    slug = SlugField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'contract',
            'target_dscp',
            'qos_priority',
            'apply_both_directions',
            'reverse_filter_ports',
        ),
    )

    class Meta:
        model = contract_subject_model.ContractSubject
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'contract',
            'target_dscp',
            'qos_priority',
            'apply_both_directions',
            'reverse_filter_ports',
        )
