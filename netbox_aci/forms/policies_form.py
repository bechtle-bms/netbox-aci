"""
Define the django form elements for the user interface. 
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from ..models import policies_model

__all__ = (
    "LinkLevelForm",
    "CDPForm",
    "LLDPForm",
    "PortChannelForm",
)


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
        model = policies_model.LinkLevel
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'negotiation',
            'speed',
        )


class CDPForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'admin_state',
        ),
    )

    class Meta:
        model = policies_model.CDP
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'admin_state',
        )


class LLDPForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'receive_state',
            'transmit_state',
        ),
    )

    class Meta:
        model = policies_model.LLDP
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'receive_state',
            'transmit_state',
        )


class PortChannelForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'mode',
        ),
    )

    class Meta:
        model = policies_model.PortChannel
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'mode',
        )
