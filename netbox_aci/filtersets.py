from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from . models import epg_model, esg_model, bd_model, aaep_model, ipg_model


class EndPointGroupListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = epg_model.EndPointGroup
        fields = ['id',
                  'name',
                  'description',
                  'applicationprofile',
                  'domains',
                  'contracts_consume',
                  'contracts_provide'
                  ]

    def search(self, queryset, name, value):
        query = (
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(applicationprofile__name__icontains=value) |
            Q(domains__name__icontains=value) |
            Q(contracts_consume__name__icontains=value) |
            Q(contracts_provide__name__icontains=value)
            )
        return queryset.filter(query)


class EndPointSecurityGroupListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = esg_model.EndPointSecurityGroup
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

    def search(self, queryset, name, value):
        query = (
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
        return queryset.filter(query)


class BridgeDomainListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = bd_model.BridgeDomain
        fields = ['id', 'name', 'description', 'vrf', 'l3outs']

    def search(self, queryset, name, value):
        query = (
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(vrf__name__icontains=value) |
            Q(l3outs__name__icontains=value)
            )
        return queryset.filter(query)


class AAEPListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = aaep_model.AAEP
        fields = ['id', 'name', 'description', 'domains']

    def search(self, queryset, name, value):
        query = (
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(domains__name__icontains=value)
            )
        return queryset.filter(query)


class PolicyGroupListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = ipg_model.PolicyGroup
        fields = ['id', 'name', 'description', 'aaep']

    def search(self, queryset, name, value):
        query = (
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(aaep__name__icontains=value)
            )
        return queryset.filter(query)
