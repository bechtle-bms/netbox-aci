"""
Define the django form elements for the user interface. 
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import SlugField
from utilities.forms.rendering import FieldSet
from .. models import contract_filter_model


class ContractFilterForm(NetBoxModelForm):

    slug = SlugField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'contractsubject',
            'directives',
            'action',
        ),
    )

    class Meta:
        model = contract_filter_model.ContractFilter
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'contractsubject',
            'directives',
            'action',
        )
