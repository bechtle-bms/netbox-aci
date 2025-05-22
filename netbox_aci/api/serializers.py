from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from tenancy.api.serializers import TenantSerializer
from ipam.api.serializers import VLANGroupSerializer, VRFSerializer, IPAddressSerializer, PrefixSerializer
from extras.api.serializers import TagSerializer
from dcim.api.serializers import DeviceSerializer, InterfaceSerializer
from .. import models


class ApplicationProfileSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:applicationprofile-detail',
    )

    tenant = TenantSerializer(nested=True)

    class Meta:
        model = models.ap_model.ApplicationProfile
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'created',
            'last_updated',
            'url',
            'tenant',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class ContractSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:contract-detail',
    )

    vrfs_consume = VRFSerializer(nested=True, many=True, required=False, allow_null=True)
    vrfs_provide = VRFSerializer(nested=True, many=True, required=False, allow_null=True)

    class Meta:
        model = models.contract_model.Contract
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'scope',
            'qos_class',
            'target_dscp',
            'vrfs_consume',
            'vrfs_provide',
            'created',
            'last_updated',
            'url',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class ContractSubjectSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:contractsubject-detail',
    )

    contract = ContractSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = models.contract_subject_model.ContractSubject
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'contract',
            'qos_priority',
            'target_dscp',
            'apply_both_directions',
            'reverse_filter_ports',            
            'created',
            'last_updated',
            'url',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class ContractFilterSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:contractfilter-detail',
    )

    contractsubject = ContractSubjectSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = models.contract_filter_model.ContractFilter
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'contractsubject',
            'directives',
            'action',
            'created',
            'last_updated',
            'url',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class ContractFilterEntrySerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:contractfilterentry-detail',
    )

    contractfilter = ContractFilterSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = models.contract_filter_entry_model.ContractFilterEntry
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'contractfilter',
            'ether_type',
            'ip_protocol',
            'arp_flag',
            'sport_from',
            'sport_to',
            'dport_from',
            'dport_to',
            'created',
            'last_updated',
            'url',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class L3OutSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:l3out-detail',
    )

    vrf = VRFSerializer(nested=True, required=False, allow_null=True)
    domains = VLANGroupSerializer(nested=True, many=True, required=False, allow_null=True)

    class Meta:
        model = models.l3out_model.L3Out
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',            
            'created',
            'last_updated',
            'url',
            'vrf',
            'domains',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class BridgeDomainSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:bridgedomain-detail',
    )

    vrf = VRFSerializer(nested=True, required=False, allow_null=True)
    subnets = IPAddressSerializer(nested=True, many=True, required=False, allow_null=True)
    l3outs = L3OutSerializer(nested=True, many=True, required=False, allow_null=True)

    class Meta:
        model = models.bd_model.BridgeDomain
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',            
            'vrf',
            'l2_unknown_unicast',
            'arp_flooding',
            'unicast_routing',
            'subnets',
            'l3outs',
            'created',
            'last_updated',
            'url',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class EndPointGroupSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:endpointgroup-detail',
    )

    applicationprofile = ApplicationProfileSerializer(nested=True)
    bridgedomain = BridgeDomainSerializer(nested=True, required=False, allow_null=True)
    subnets = IPAddressSerializer(nested=True, many=True, required=False, allow_null=True)
    domains = VLANGroupSerializer(nested=True, many=True, required=False, allow_null=True)
    contracts_provide = ContractSerializer(nested=True, many=True, required=False, allow_null=True)
    contracts_consume = ContractSerializer(nested=True, many=True, required=False, allow_null=True)

    class Meta:
        model = models.epg_model.EndPointGroup
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',            
            'created',
            'last_updated',
            'url',
            'applicationprofile',
            'domains',
            'contracts_provide',
            'contracts_consume',
            'bridgedomain',
            'subnets',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class EndPointSecurityGroupSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:endpointsecuritygroup-detail',
    )

    contracts_provide = ContractSerializer(nested=True, many=True, required=False, allow_null=True)
    contracts_consume = ContractSerializer(nested=True, many=True, required=False, allow_null=True)
    epgs_selector = EndPointGroupSerializer(nested=True, many=True, required=False, allow_null=True)
    ip_subnets_selector = PrefixSerializer(nested=True, many=True, required=False, allow_null=True)
    tags_selector = TagSerializer(nested=True, many=True, required=False, allow_null=True)
    vrf = VRFSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = models.esg_model.EndPointSecurityGroup
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',            
            'vrf',
            'created',
            'last_updated',
            'url',
            'applicationprofile',
            'contracts_provide',
            'contracts_consume',
            'epgs_selector',
            'ip_subnets_selector',
            'tags_selector',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class DomainSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:domain-detail',
    )

    vlan_pool = VLANGroupSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = models.domain_model.Domain
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'domain_type',          
            'vlan_pool',
            'pool_allocation_mode',
            'created',
            'last_updated',
            'url',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class AAEPSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:aaep-detail',
    )

    domains = VLANGroupSerializer(nested=True, many=True, required=False, allow_null=True)

    class Meta:
        model = models.aaep_model.AAEP
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',            
            'created',
            'last_updated',
            'url',
            'infrastructure_vlan',
            'domains',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class AAEPStaticBindingSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:aaepstaticbinding-detail',
    )

    aaep = AAEPSerializer(nested=True)
    tenant = TenantSerializer(nested=True)
    applicationprofile = ApplicationProfileSerializer(nested=True)
    epg = EndPointGroupSerializer(nested=True)

    class Meta:
        model = models.aaep_model.AAEPStaticBinding
        fields = (
            'id',
            'aaep',
            'created',
            'last_updated',
            'tenant',
            'applicationprofile',
            'epg',
            'encap',
            'mode',
        )
        brief_fields = ("id", "url")


class LinkLevelSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:linklevel-detail',
    )

    class Meta:
        model = models.policy_link_level_model.LinkLevel
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'created',
            'last_updated',
            'url',
            'negotiation',
            'speed',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class PolicyGroupSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:policygroup-detail',
    )

    aaep = AAEPSerializer(nested=True)
    linklevel = LinkLevelSerializer(nested=True)

    class Meta:
        model = models.ipg_model.PolicyGroup
        fields = (
            'id',
            'display',
            'name',
            'slug',
            'description',
            'created',
            'last_updated',
            'url',
            'aaep',
            'linklevel',
        )
        brief_fields = ("id", "display", "name", "slug", "url")


class PolicyGroupAssignementSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_aci-api:policygroupassignement-detail',
    )

    ipg = PolicyGroupSerializer(nested=True)
    device = DeviceSerializer(nested=True)
    interface = InterfaceSerializer(nested=True)

    class Meta:
        model = models.ipg_model.PolicyGroupAssignement
        fields = (
            'id',
            'ipg',
            'device',
            'interface',
            'created',
            'last_updated',            
        )
        brief_fields = ("id", "url")
