"""
Define the logic of the plugin.
"""

from django.shortcuts import render
from django.views.generic import View
from ipam.models import vlans
from netbox.views import generic
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view

from .. import tables
from .. models import domain_model
from .. forms import domain_form

__all__ = (
    "DomainView",
    "DomainListView",
    "DomainEditView",
    "DomainDeleteView",
    "DomainBulkDeleteView",
    "DomainIpamVlangroupTabView",
)


class DomainView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = domain_model.Domain.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'vlan_pool': instance.vlan_pool,
            'related_models': self.get_related_models(request, instance),
        }


class DomainListView(generic.ObjectListView):
    queryset = domain_model.Domain.objects.all()
    table = tables.DomainTable


class DomainEditView(generic.ObjectEditView):
    queryset = domain_model.Domain.objects.all()
    form = domain_form.DomainForm
    default_return_url = 'plugins:netbox_aci:domain_list'


class DomainDeleteView(generic.ObjectDeleteView):
    queryset = domain_model.Domain.objects.all()


class DomainBulkDeleteView(generic.BulkDeleteView):
    queryset = domain_model.Domain.objects.all()
    table = tables.DomainTable


@register_model_view(vlans.VLANGroup, "domains")
class DomainIpamVlangroupTabView(View):
    tab = ViewTab(
        label="ACI Domain Assignements",
        badge=lambda obj: domain_model.Domain.objects.filter(
            vlan_pool=obj
        ).count(),
        hide_if_empty = True,
        permission="netbox_aci.view_domain",
    )

    def get(self, request, pk):
        group = vlans.VLANGroup.objects.get(pk=pk)
        pool = domain_model.Domain.objects.filter(vlan_pool=group)

        return render(
            request,
            "netbox_aci/domain_tab.html",
            context={
                "tab": self.tab,
                "object": group,
                "domain_table": pool,
            },
        )
