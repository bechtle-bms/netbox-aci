"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable

from .. models import domain_model

__all__ = (
    "DomainTable",
)


class DomainTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    vlan_pool = tables.Column(
        linkify = True,
    )

    class Meta(NetBoxTable.Meta):
        model = domain_model.Domain
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "domain_type",
            "vlan_pool",
            "pool_allocation_mode",
        )
        default_columns = (
            "name",
            "domain_type",
            "vlan_pool",
            "pool_allocation_mode",
        )
