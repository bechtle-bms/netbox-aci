"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .. models import aaep_model

__all__ = (
    "AAEPTable",
    "AAEPStaticBindingTable",
)


class AAEPTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    domains = columns.ManyToManyColumn(
        linkify_item = True,
    )

    epg = columns.ManyToManyColumn(
        linkify_item = True,
    )

    class Meta(NetBoxTable.Meta):
        model = aaep_model.AAEP
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "infrastructure_vlan",
            "domains",
        )
        default_columns = (
            "name",
            "domains",
        )


class AAEPStaticBindingTable(NetBoxTable):

    tenant = tables.Column(
        linkify=True
    )

    applicationprofile = tables.Column(
        linkify=True
    )

    epg = tables.Column(
        linkify = True,
    )

    class Meta(NetBoxTable.Meta):
        model = aaep_model.AAEPStaticBinding
        fields = (
            "tenant",
            "applicationprofile",
            "epg",
            "encap",
            "mode",
        )
        default_columns = (
            "tenant",
            "applicationprofile",
            "epg",
            "encap",
            "mode",
        )
