from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from . import models


class ApplicationProfileListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.ap_model.ApplicationProfile
        fields = ['id',
                  'name',
                  'description',
                  'tenant'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(tenant__name__icontains=value)
        )


class EndPointGroupListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.epg_model.EndPointGroup
        fields = ['id',
                  'name',
                  'description',
                  'applicationprofile',
                  'domains',
                  'contracts_consume',
                  'contracts_provide'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(applicationprofile__name__icontains=value) |
            Q(domains__name__icontains=value) |
            Q(contracts_consume__name__icontains=value) |
            Q(contracts_provide__name__icontains=value)
        )


class ContractListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.contract_model.Contract
        fields = ['id',
                  'name',
                  'description',
                  'scope',
                  'vrfs_consume',
                  'vrfs_provide'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(scope__name__icontains=value) |
            Q(vrfs_consume__name__icontains=value) |
            Q(vrfs_provide__name__icontains=value)
        )


class ContractSubjectListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.contract_subject_model.ContractSubject
        fields = ['id',
                  'name',
                  'description',
                  'contract'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(contract__name__icontains=value)
        )


class ContractFilterListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.contract_filter_model.ContractFilter
        fields = ['id',
                  'name',
                  'description',
                  'contractsubject'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(contractsubject__name__icontains=value)
        )


class ContractFilterEntryListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.contract_filter_entry_model.ContractFilterEntry
        fields = ['id',
                  'name',
                  'description',
                  'contractfilter',
                  'ether_type',
                  'ip_protocol'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(contractfilter__name__icontains=value) |
            Q(ether_type__icontains=value) |
            Q(ip_protocol__icontains=value)
        )


class BridgeDomainListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.bd_model.BridgeDomain
        fields = ['id',
                  'name',
                  'description',
                  'vrf',
                  'l3outs'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(vrf__name__icontains=value) |
            Q(l3outs__name__icontains=value)
        )


class EndPointSecurityGroupListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.esg_model.EndPointSecurityGroup
        fields = ['id',
                  'name',
                  'description',
                  'applicationprofile',
                  'vrf',
                  'contracts_consume',
                  'contracts_provide',
                  'epgs_selector',
                  'ip_subnets_selector',
                  'tags_selector'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(applicationprofile__name__icontains=value) |
            Q(vrf__name__icontains=value) |
            Q(contracts_consume__name__icontains=value) |
            Q(contracts_provide__name__icontains=value) |
            Q(epgs_selector__name__icontains=value) |
            Q(ip_subnets_selector__name__icontains=value) |
            Q(tags_selector__name__icontains=value)
        )


class L3OutListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.l3out_model.L3Out
        fields = ['id',
                  'name',
                  'description',
                  'vrf',
                  'domains'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(vrf__name__icontains=value) |
            Q(domains__name__icontains=value)
        )


class DomainFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.domain_model.Domain
        fields = ['id',
                  'name',
                  'description',
                  'domain_type',
                  'vlan_pool',
                  'pool_allocation_mode'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(domain_type_icontains=value) |
            Q(vlan_pool__name__icontains=value) |
            Q(pool_allocation_mode__name__icontains=value)
        )


class AAEPListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.aaep_model.AAEP
        fields = ['id',
                  'name',
                  'description',
                  'domains'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(domains__name__icontains=value)
        )


class AAEPStaticBindingListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.aaep_model.AAEPStaticBinding
        fields = ['id',
                  'aaep',
                  'tenant',
                  'applicationprofile',
                  'epg',
                  'encap'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(aaep__name__icontains=value) |
            Q(tenant__name__icontains=value) |
            Q(applicationprofile__name__icontains=value) |
            Q(epg__name__icontains=value) |
            Q(encap__icontains=value)
        )


class PolicyGroupListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.ipg_model.PolicyGroup
        fields = ['id',
                  'name',
                  'description',
                  'type',
                  'aaep'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset        
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(type__icontains=value) |
            Q(aaep__name__icontains=value)
        )


class PolicyGroupLAssignementistFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.ipg_model.PolicyGroupAssignement
        fields = ['id',
                  'ipg',
                  'device',
                  'interface'
        ]

    def search(self, queryset, value):
        if not value.strip():
            return queryset        
        return queryset.filter(
            Q(ipg__name__icontains=value) |
            Q(device__name__icontains=value) |
            Q(interface__name__icontains=value)
        )
