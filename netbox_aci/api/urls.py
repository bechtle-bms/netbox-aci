"""
Creates API endpoint URLs for the plugin.
"""

from netbox.api.routers import NetBoxRouter

from . import views

app_name = "netbox_aci"

router = NetBoxRouter()
router.register("applicationprofile", views.ApplicationProfileViewSet)
router.register("endpointgroup", views.EndPointGroupViewSet)
router.register("endpointsecuritygroup", views.EndPointSecurityGroupViewSet)
router.register("contract", views.ContractViewSet)
router.register("contractsubject", views.ContractSubjectViewSet)
router.register("contractfilter", views.ContractFilterViewSet)
router.register("contractfilterentry", views.ContractFilterEntryViewSet)
router.register("bridgedomain", views.BridgeDomainViewSet)
router.register("l3out", views.L3OutViewSet)
router.register("domain", views.DomainViewSet)
router.register("aaep", views.AAEPViewSet)
router.register("aaepstaticbinding", views.AAEPStaticBindingViewSet)
router.register("policygroup", views.PolicyGroupViewSet)
router.register("policygroupassignement", views.PolicyGroupAssignementViewSet)
router.register("linklevel", views.LinkLevelViewSet)

urlpatterns = router.urls
