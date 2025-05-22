"""
Define the django form elements for the user interface. 
"""

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from .. models import ap_model


class ApplicationProfileForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'tenant',
        ),
    )

    class Meta:
        model = ap_model.ApplicationProfile
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'tenant',
        )
