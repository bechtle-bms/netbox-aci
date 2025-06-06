"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable

from .. models import ipg_model

__all__ = (
    "IPGTable",
    "IPGAssignementTable",
)


class IPGTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    aaep = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = ipg_model.PolicyGroup
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "type",
            "aaep",
        )
        default_columns = (
            "name",
            "type",
            "aaep",
        )


class IPGAssignementTable(NetBoxTable):

    ipg = tables.Column(
        linkify=True
    )

    device = tables.Column(
        linkify=True
    )

    interface = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = ipg_model.PolicyGroupAssignement
        fields = (
            "ipg",
            "device",
            "interface",
        )
        default_columns = (
            "ipg",
            "device",
            "interface",            
        )
