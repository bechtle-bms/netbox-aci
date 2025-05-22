from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet

from .. import models

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
    )


class ApplicationProfileViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ApplicationProfile model & associates it to a view.
    """

    queryset = models.ap_model.ApplicationProfile.objects.all()
    serializer_class = ApplicationProfileSerializer


class EndPointGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django EndPointGroup model & associates it to a view.
    """

    queryset = models.epg_model.EndPointGroup.objects.all()
    serializer_class = EndPointGroupSerializer


class ContractViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Contract model & associates it to a view.
    """

    queryset = models.contract_model.Contract.objects.all()
    serializer_class = ContractSerializer


class ContractSubjectViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ContractSubject model & associates it to a view.
    """

    queryset = models.contract_subject_model.ContractSubject.objects.all()
    serializer_class = ContractSubjectSerializer


class ContractFilterViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ContractFilter model & associates it to a view.
    """

    queryset = models.contract_filter_model.ContractFilter.objects.all()
    serializer_class = ContractFilterSerializer


class ContractFilterEntryViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django ContractFilter model & associates it to a view.
    """

    queryset = models.contract_filter_entry_model.ContractFilterEntry.objects.all()
    serializer_class = ContractFilterEntrySerializer


class BridgeDomainViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Contract model & associates it to a view.
    """

    queryset = models.bd_model.BridgeDomain.objects.all()
    serializer_class = BridgeDomainSerializer


class EndPointSecurityGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django EndPointSecurityGroup model & associates it to a view.
    """

    queryset = models.esg_model.EndPointSecurityGroup.objects.all()
    serializer_class = EndPointSecurityGroupSerializer


class L3OutViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django L3Out model & associates it to a view.
    """

    queryset = models.l3out_model.L3Out.objects.all()
    serializer_class = L3OutSerializer


class DomainViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Domain model & associates it to a view.
    """

    queryset = models.domain_model.Domain.objects.all()
    serializer_class = DomainSerializer


class AAEPViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django AAEP model & associates it to a view.
    """

    queryset = models.aaep_model.AAEP.objects.all()
    serializer_class = AAEPSerializer


class AAEPStaticBindingViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django AAEP static binding model & associates it to a view.
    """

    queryset = models.aaep_model.AAEPStaticBinding.objects.all()
    serializer_class = AAEPStaticBindingSerializer


class PolicyGroupViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface Policy Group model & associates it to a view.
    """

    queryset = models.ipg_model.PolicyGroup.objects.all()
    serializer_class = PolicyGroupSerializer


class PolicyGroupAssignementViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface Policy Group Assignement model & associates it to a view.
    """

    queryset = models.ipg_model.PolicyGroupAssignement.objects.all()
    serializer_class = PolicyGroupAssignementSerializer


class LinkLevelViewSet(NetBoxModelViewSet):
    """
    Defines the view set for the django Interface Link Level Policy & associates it to a view.
    """

    queryset = models.policy_link_level_model.LinkLevel.objects.all()
    serializer_class = LinkLevelSerializer
