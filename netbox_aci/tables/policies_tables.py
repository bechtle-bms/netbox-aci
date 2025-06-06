"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable

from .. models import policies_model

__all__ = (
    "LinkLevelTable",
    "CDPTable",
    "LLDPTable",
    "PortChannelTable"
)


class LinkLevelTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    tenant = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = policies_model.LinkLevel
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "negotiation",
            "speed",
        )
        default_columns = (
            "name",
            "negotiation",
            "speed",
        )


class CDPTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    admin_state = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = policies_model.CDP
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "admin_state",
        )
        default_columns = (
            "name",
            "admin_state",
        )


class LLDPTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    admin_state = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = policies_model.LLDP
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "receive_state",
            "transmit_state",
        )
        default_columns = (
            "name",
            "receive_state",
            "transmit_state",
        )


class PortChannelTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    admin_state = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = policies_model.PortChannel
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "mode",
        )
        default_columns = (
            "name",
            "mode",
        )
