"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .. models import epg_model

__all__ = (
    "EndPointGroupTable",
)


class EndPointGroupTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    applicationprofile = tables.Column(
        linkify=True
    )

    domains = columns.ManyToManyColumn(
        linkify_item = True,
    )

    contracts_consume = columns.ManyToManyColumn(
        linkify_item = True,
    )

    contracts_provide = columns.ManyToManyColumn(
        linkify_item = True,
    )

    bridgedomain = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = epg_model.EndPointGroup
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "applicationprofile",
            "domains",
            "contracts_consume",
            "contracts_provide",
            "bridgedomain",
            "subnets",
        )
        default_columns = (
            "name",
            "applicationprofile",
            "domains",
            "contracts_consume",
            "contracts_provide",
            "bridgedomain",
        )
