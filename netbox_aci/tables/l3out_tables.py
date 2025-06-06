"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .. models import l3out_model

__all__ = (
    "L3OutTable",
)


class L3OutTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    vrf = tables.Column(
        linkify=True
    )

    domains = columns.ManyToManyColumn(
        linkify_item = True,
    )

    class Meta(NetBoxTable.Meta):
        model = l3out_model.L3Out
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "vrf",
            "domains",
        )
        default_columns = (
            "name",
            "vrf",
            "domains",            
        )
