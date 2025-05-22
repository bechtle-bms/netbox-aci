"""
Define the django form elements for the user interface. 
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet, TabbedGroups
from .. models import contract_model

class ContractForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            TabbedGroups(
                FieldSet(
                    'name',
                    'slug',
                    'description',
                    'scope',
                    'qos_class',
                    'target_dscp',
                    name = 'Contract',
                ),
                FieldSet(
                    'vrfs_consume',
                    'vrfs_provide',
                    name = 'vzAny',
                ),
            ),
        ),
    )

    class Meta:
        model = contract_model.Contract
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'scope',
            'qos_class',
            'target_dscp',
            'vrfs_consume',
            'vrfs_provide',
        )
