"""
Define the tables
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from . import models

__all__ = (
    "ApplicationProfileTable",
    "EndPointGroupTable",
    "ContractTable",
    "ContractSubjectTable",
    "ContractFilterTable",
    "BridgeDomainTable",
    "L3OutTable",
    "DomainTable",
    "AAEPTable",
    "AAEPStaticBindingTable",
    "IPGTable",
    "IPGAssignementTable",
    "LinkLevelTable",
)


class ApplicationProfileTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    tenant = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = models.ap_model.ApplicationProfile
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
        model = models.epg_model.EndPointGroup
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
        model = models.esg_model.EndPointSecurityGroup
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
        model = models.contract_model.Contract
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


class VrfContractTabTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = models.contract_model.Contract
        fields = (
            "name",
            "slug",
            "description",
            "comments",
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
        model = models.contract_subject_model.ContractSubject
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
        model = models.contract_filter_model.ContractFilter
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
        model = models.contract_filter_entry_model.ContractFilterEntry
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
        model = models.bd_model.BridgeDomain
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
        model = models.l3out_model.L3Out
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


class DomainTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    vlan_pool = tables.Column(
        linkify = True,
    )

    class Meta(NetBoxTable.Meta):
        model = models.domain_model.Domain
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
        model = models.aaep_model.AAEP
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
        model = models.aaep_model.AAEPStaticBinding
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


class IPGTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    aaep = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = models.ipg_model.PolicyGroup
        fields = (
            "name",
            "slug",
            "description",
            "comments",
            "aaep",
        )
        default_columns = (
            "name",
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
        model = models.ipg_model.PolicyGroupAssignement
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


class LinkLevelTable(NetBoxTable):

    name = tables.Column(
        linkify=True
    )

    tenant = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = models.policy_link_level_model.LinkLevel
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
