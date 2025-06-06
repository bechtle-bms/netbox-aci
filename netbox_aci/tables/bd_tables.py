"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .. models import bd_model

__all__ = (
    "BridgeDomainTable",
)


class BridgeDomainTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    vrf = tables.Column(
        linkify=True
    )

    subnets = columns.ManyToManyColumn(
        linkify_item = True,
    )

    l3outs = columns.ManyToManyColumn(
        linkify_item = True,
    )

    class Meta(NetBoxTable.Meta):
        model = bd_model.BridgeDomain
        fields = (
            "name",
            "slug",
            "description",
            "comments",            
            "vrf",
            "l2_unknown_unicast",
            "arp_flooding",
            "unicast_routing",
            "subnets",
            "l3outs",
            "comments",
        )
        default_columns = (
            "name",
            "vrf",
            "l2_unknown_unicast",
            "arp_flooding",
            "unicast_routing",
            "subnets",
            "l3outs",
        )
