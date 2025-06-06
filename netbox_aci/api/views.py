from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models

from . serializers import (
    ApplicationProfileSerializer,
    EndPointGroupSerializer,
    ContractSerializer,
    ContractSubjectSerializer,
    ContractFilterSerializer,
    ContractFilterEntrySerializer,
    BridgeDomainSerializer,
    EndPointSecurityGroupSerializer,
    L3OutSerializer,
    DomainSerializer,
    AAEPSerializer,
    AAEPStaticBindingSerializer,
    PolicyGroupSerializer,
    PolicyGroupAssignementSerializer,
    LinkLevelSerializer,
    CDPSerializer,
    LLDPSerializer,
    PortChannelSerializer
    )


class ApplicationProfileViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ApplicationProfile model & associates it to a view.
    """
    queryset = models.ap_model.ApplicationProfile.objects.all()
    serializer_class = ApplicationProfileSerializer
    filterset_class = filtersets.ApplicationProfileListFilterSet


class EndPointGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django EndPointGroup model & associates it to a view.
    """
    queryset = models.epg_model.EndPointGroup.objects.all()
    serializer_class = EndPointGroupSerializer
    filterset_class = filtersets.EndPointGroupListFilterSet


class ContractViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Contract model & associates it to a view.
    """
    queryset = models.contract_model.Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_class = filtersets.ContractListFilterSet


class ContractSubjectViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ContractSubject model & associates it to a view.
    """
    queryset = models.contract_subject_model.ContractSubject.objects.all()
    serializer_class = ContractSubjectSerializer
    filterset_class = filtersets.ContractSubjectListFilterSet


class ContractFilterViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ContractFilter model & associates it to a view.
    """
    queryset = models.contract_filter_model.ContractFilter.objects.all()
    serializer_class = ContractFilterSerializer
    filterset_class = filtersets.ContractFilterListFilterSet


class ContractFilterEntryViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ContractFilterEntry model & associates it to a view.
    """
    queryset = models.contract_filter_entry_model.ContractFilterEntry.objects.all()
    serializer_class = ContractFilterEntrySerializer
    filterset_class = filtersets.ContractFilterEntryListFilterSet


class BridgeDomainViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django BridgeDomain model & associates it to a view.
    """
    queryset = models.bd_model.BridgeDomain.objects.all()
    serializer_class = BridgeDomainSerializer
    filterset_class = filtersets.BridgeDomainListFilterSet


class EndPointSecurityGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django EndPointSecurityGroup model & associates it to a view.
    """
    queryset = models.esg_model.EndPointSecurityGroup.objects.all()
    serializer_class = EndPointSecurityGroupSerializer
    filterset_class = filtersets.EndPointSecurityGroupListFilterSet


class L3OutViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django L3Out model & associates it to a view.
    """
    queryset = models.l3out_model.L3Out.objects.all()
    serializer_class = L3OutSerializer
    filterset_class = filtersets.L3OutListFilterSet


class DomainViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Domain model & associates it to a view.
    """
    queryset = models.domain_model.Domain.objects.all()
    serializer_class = DomainSerializer
    filterset_class = filtersets.DomainFilterSet


class AAEPViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django AAEP model & associates it to a view.
    """
    queryset = models.aaep_model.AAEP.objects.all()
    serializer_class = AAEPSerializer
    filterset_class = filtersets.AAEPListFilterSet


class AAEPStaticBindingViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django AAEP static binding model & associates it to a view.
    """
    queryset = models.aaep_model.AAEPStaticBinding.objects.all()
    serializer_class = AAEPStaticBindingSerializer
    filterset_class = filtersets.AAEPStaticBindingListFilterSet


class PolicyGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface Policy Group model & associates it to a view.
    """
    queryset = models.ipg_model.PolicyGroup.objects.all()
    serializer_class = PolicyGroupSerializer
    filterset_class = filtersets.PolicyGroupListFilterSet


class PolicyGroupAssignementViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface Policy Group Assignement model & associates it to a view.
    """
    queryset = models.ipg_model.PolicyGroupAssignement.objects.all()
    serializer_class = PolicyGroupAssignementSerializer
    filterset_class = filtersets.PolicyGroupLAssignementistFilterSet


class LinkLevelViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface Link Level Policy & associates it to a view.
    """
    queryset = models.policies_model.LinkLevel.objects.all()
    serializer_class = LinkLevelSerializer


class CDPViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface CDP Policy & associates it to a view.
    """
    queryset = models.policies_model.CDP.objects.all()
    serializer_class = CDPSerializer


class LLDPViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface LLDP Policy & associates it to a view.
    """
    queryset = models.policies_model.LLDP.objects.all()
    serializer_class = LLDPSerializer


class PortChannelViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface PortChannel Policy & associates it to a view.
    """
    queryset = models.policies_model.PortChannel.objects.all()
    serializer_class = PortChannelSerializer
