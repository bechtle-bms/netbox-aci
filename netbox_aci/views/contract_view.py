"""
Define the logic of the plugin.
"""

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from ipam.models import vrfs
from netbox.views import generic
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view
from .. import tables
from .. models import contract_model
from .. forms import contract_form

__all__ = (
    "ContractView",
    "ContractListView",
    "ContractEditView",
    "ContractDeleteView",
    "ContractBulkDeleteView",
    "ContractIpamVrfTabView",
)


class ContractView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = contract_model.Contract.objects.all()

    def get_extra_context(self, request, instance):

        contractsubject = instance.subject_contract.all()
        subject_table = tables.ContractSubjectTable(contractsubject)
        return {
            'subject_table': subject_table,
            'vrf_consume_table': instance.vrfs_consume.all(),
            'vrf_provide_table': instance.vrfs_provide.all(),
            'related_models': self.get_related_models(request, instance),
        }


class ContractListView(generic.ObjectListView):
    queryset = contract_model.Contract.objects.all()
    table = tables.ContractTable


class ContractEditView(generic.ObjectEditView):
    queryset = contract_model.Contract.objects.all()
    form = contract_form.ContractForm
    default_return_url = 'plugins:netbox_aci:contract_list'


class ContractDeleteView(generic.ObjectDeleteView):
    queryset = contract_model.Contract.objects.all()


class ContractBulkDeleteView(generic.BulkDeleteView):
    queryset = contract_model.Contract.objects.all()
    table = tables.ContractTable


@register_model_view(vrfs.VRF, "vzany")
class ContractIpamVrfTabView(View):
    tab = ViewTab(
        label="ACI vzAny Assignements",
        badge=lambda obj: contract_model.Contract.objects.filter(
            Q(vrfs_consume=obj) |
            Q(vrfs_provide=obj)
        ).count(),
        hide_if_empty = True,
        permission="netbox_aci.view_contract",
    )

    def get(self, request, pk):
        vrf = vrfs.VRF.objects.get(pk=pk)
        contract_consume = contract_model.Contract.objects.filter(vrfs_consume=vrf)
        contract_provide = contract_model.Contract.objects.filter(vrfs_provide=vrf)

        return render(
            request,
            "netbox_aci/contract_tab.html",
            context={
                "tab": self.tab,
                "object": vrf,
                "vrf_consume_table": contract_consume,
                "vrf_provide_table": contract_provide,
            },
        )
