from netbox.search import SearchIndex, register_search
from . models import aaep_model, ap_model, bd_model, contract_model, domain_model, epg_model, esg_model, ipg_model, l3out_model

@register_search
class AAEPIndex(SearchIndex):
    model = aaep_model.AAEP
    fields = (
        ('name', 100),
    )

@register_search
class ApplicationProfileIndex(SearchIndex):
    model = ap_model.ApplicationProfile
    fields = (
        ('name', 100),
    )

@register_search
class BridgeDomainIndex(SearchIndex):
    model = bd_model.BridgeDomain
    fields = (
        ('name', 100),
    )

@register_search
class ContractIndex(SearchIndex):
    model = contract_model.Contract
    fields = (
        ('name', 100),
    )

@register_search
class DomainIndex(SearchIndex):
    model = domain_model.Domain
    fields = (
        ('name', 100),
    )

@register_search
class EPGIndex(SearchIndex):
    model = epg_model.EndPointGroup
    fields = (
        ('name', 100),
    )

@register_search
class ESGIndex(SearchIndex):
    model = esg_model.EndPointSecurityGroup
    fields = (
        ('name', 100),
    )

@register_search
class IPGIndex(SearchIndex):
    model = ipg_model.PolicyGroup
    fields = (
        ('name', 100),
    )

@register_search
class L3OutIndex(SearchIndex):
    model = l3out_model.L3Out
    fields = (
        ('name', 100),
    )
