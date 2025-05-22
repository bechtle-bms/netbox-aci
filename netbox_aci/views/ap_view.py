"""
Define the logic of the plugin.
"""

from django.shortcuts import render
from django.views.generic import View
from tenancy.models import tenants
from netbox.views import generic
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view

from .. import tables
from .. models import ap_model
from .. forms import ap_form

__all__ = (
    "ApplicationProfileView",
    "ApplicationProfileListView",
    "ApplicationProfileEditView",
    "ApplicationProfileDeleteView",
    "ApplicationProfileBulkDeleteView",
    "ApplicationProfileTenancyTenantTabView",
)


class ApplicationProfileView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = ap_model.ApplicationProfile.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class ApplicationProfileListView(generic.ObjectListView):
    queryset = ap_model.ApplicationProfile.objects.all()
    table = tables.ApplicationProfileTable


class ApplicationProfileEditView(generic.ObjectEditView):
    queryset = ap_model.ApplicationProfile.objects.all()
    form = ap_form.ApplicationProfileForm
    default_return_url = 'plugins:netbox_aci:applicationprofile_list'


class ApplicationProfileDeleteView(generic.ObjectDeleteView):
    queryset = ap_model.ApplicationProfile.objects.all()


class ApplicationProfileBulkDeleteView(generic.BulkDeleteView):
    queryset = ap_model.ApplicationProfile.objects.all()
    table = tables.ApplicationProfileTable


@register_model_view(tenants.Tenant, "applicationprofiles")
class ApplicationProfileTenancyTenantTabView(View):
    tab = ViewTab(
        label="ACI Applicationprofile Assignements",
        badge=lambda obj: ap_model.ApplicationProfile.objects.filter(
            tenant=obj
        ).count(),
        hide_if_empty = True,
        permission="netbox_aci.view_applicationprofile",
    )

    def get(self, request, pk):
        tnt = tenants.Tenant.objects.get(pk=pk)
        anp = ap_model.ApplicationProfile.objects.filter(tenant=tnt)

        return render(
            request,
            "netbox_aci/applicationprofile_tab.html",
            context={
                "tab": self.tab,
                "object": tnt,
                "anp_table": anp,
            },
        )
