"""
Define the django form elements for the user interface. 
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from .. models import policy_link_level_model


class LinkLevelForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'negotiation',
            'speed',
        ),
    )

    class Meta:
        model = policy_link_level_model.LinkLevel
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'negotiation',
            'speed',
        )
