"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable

from .. models import ap_model

__all__ = (
    "ApplicationProfileTable",
)


class ApplicationProfileTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    tenant = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = ap_model.ApplicationProfile
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "tenant",
        )
        default_columns = (
            "name",
            "tenant",
        )
