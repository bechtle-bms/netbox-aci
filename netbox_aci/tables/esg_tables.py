"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .. models import esg_model

__all__ = (
    "EndPointSecurityGroupTable",
)


class EndPointSecurityGroupTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    vrf = tables.Column(
        linkify=True
    )

    contracts_consume = columns.ManyToManyColumn(
        linkify_item = True,
    )

    contracts_provide = columns.ManyToManyColumn(
        linkify_item = True,
    )

    epgs_selector = columns.ManyToManyColumn(
        linkify=True
    )

    ip_subnets_selector = columns.ManyToManyColumn(
        linkify=True
    )

    tags_selector = columns.ManyToManyColumn(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = esg_model.EndPointSecurityGroup
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "applicationprofile",
            "vrf",
            "contracts_consume",
            "contracts_provide",
            "epgs_selector",
            "ip_subnets_selector",
            "tags_selector",
        )
        default_columns = (
            "name",
            "applicationprofile",
            "vrf",
            "contracts_consume",
            "contracts_provide",
            "epgs_selector",
            "ip_subnets_selector",
            "tags_selector",
        )
