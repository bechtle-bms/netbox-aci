"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .. models import contract_model, contract_subject_model, contract_filter_model, contract_filter_entry_model

__all__ = (
    "ContractTable",
    "ContractSubjectTable",
    "ContractFilterTable",
    "ContractFilterEntryTable",
)


class ContractTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    vrfs_consume = columns.ManyToManyColumn(
        linkify_item = True,
    )

    vrfs_provide = columns.ManyToManyColumn(
        linkify_item = True,
    )

    class Meta(NetBoxTable.Meta):
        model = contract_model.Contract
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "scope",
            "qos_class",
            "target_dscp",
            "vrfs_consume",
            "vrfs_provide",
        )
        default_columns = (
            "name",
            "scope",
        )


class ContractSubjectTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    contract = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = contract_subject_model.ContractSubject
        fields = (
            "name",
            "slug",
            "contract",
            "description",
            "comments",
            "target_dscp",
            "qos_priority",
            "apply_both_directions",
            "reverse_filter_ports",
        )
        default_columns = (
            "name",
        )


class ContractFilterTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    contractsubject = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = contract_filter_model.ContractFilter
        fields = (
            "name",
            "slug",
            "contractsubject",
            "description",
            "comments",
            "directives",
            "action",
        )
        default_columns = (
            "name",
        )


class ContractFilterEntryTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    contractfilter = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = contract_filter_entry_model.ContractFilterEntry
        fields = (
            "name",
            "slug",
            "contractfilter",
            "description",
            "comments",
            "ether_type",
            "ip_protocol",
            "arp_flag",
            "sport_from",
            "sport_to",
            "dport_from",
            "dport_to",
        )
        default_columns = (
            "name",
            "ether_type",
        )
