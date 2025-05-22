"""
Define the logic of the plugin.
"""

from django.shortcuts import render
from django.views.generic import View
from dcim.models import device_components
from netbox.views import generic
from utilities.views import GetRelatedModelsMixin, ViewTab, register_model_view

from .. import tables
from .. models import ipg_model
from .. forms import ipg_form
from .. import filtersets

__all__ = (
    "PolicyGroupView",
    "PolicyGroupListView",
    "PolicyGroupEditView",
    "PolicyGroupDeleteView",
    "PolicyGroupBulkDeleteView",
    "PolicyGroupAssignementView",
    "PolicyGroupAssignementListView",
    "PolicyGroupAssignementEditView",
    "PolicyGroupAssignementDeleteView",
    "PolicyGroupAssignementBulkDeleteView",
    "PolicyGroupDcimInterfaceTabView",
)


class PolicyGroupView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = ipg_model.PolicyGroup.objects.all()

    def get_extra_context(self, request, instance):

        ipgassignement_table = tables.IPGAssignementTable(instance.ipgassignement.all())

        return {
            'ipgassignement_table': ipgassignement_table,
            'related_models': self.get_related_models(request, instance),
        }


class PolicyGroupListView(generic.ObjectListView):
    queryset = ipg_model.PolicyGroup.objects.all()
    table = tables.IPGTable
    filterset = filtersets.PolicyGroupListFilterSet
    filterset_form = ipg_form.PolicyGroupFilterForm

class PolicyGroupEditView(generic.ObjectEditView):
    queryset = ipg_model.PolicyGroup.objects.all()
    form = ipg_form.PolicyGroupForm
    default_return_url = 'plugins:netbox_aci:policygroup_list'


class PolicyGroupDeleteView(generic.ObjectDeleteView):
    queryset = ipg_model.PolicyGroup.objects.all()


class PolicyGroupBulkDeleteView(generic.BulkDeleteView):
    queryset = ipg_model.PolicyGroup.objects.all()
    table = tables.IPGTable


class PolicyGroupAssignementView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = ipg_model.PolicyGroupAssignement.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),

        }


class PolicyGroupAssignementListView(generic.ObjectListView):
    queryset = ipg_model.PolicyGroupAssignement.objects.all()
    table = tables.IPGAssignementTable


class PolicyGroupAssignementEditView(generic.ObjectEditView):
    queryset = ipg_model.PolicyGroupAssignement.objects.all()
    form = ipg_form.PolicyGroupAssignementForm
    default_return_url = 'plugins:netbox_aci:policygroupassignement_list'


class PolicyGroupAssignementDeleteView(generic.ObjectDeleteView):
    queryset = ipg_model.PolicyGroupAssignement.objects.all()


class PolicyGroupAssignementBulkDeleteView(generic.BulkDeleteView):
    queryset = ipg_model.PolicyGroupAssignement.objects.all()
    table = tables.IPGAssignementTable


@register_model_view(device_components.Interface, "ipg")
class PolicyGroupDcimInterfaceTabView(View):
    tab = ViewTab(
        label="ACI IPG Assignements",
        badge=lambda obj: ipg_model.PolicyGroupAssignement.objects.filter(
            interface=obj
        ).count(),
        hide_if_empty = True,
        permission="netbox_aci.view_policygroup",
    )

    def get(self, request, pk):
        intf = device_components.Interface.objects.get(pk=pk)
        policy_group = ipg_model.PolicyGroupAssignement.objects.filter(interface=intf)
        ipg = ipg_model.PolicyGroup.objects.filter(ipgassignement__in=policy_group)

        return render(
            request,
            "netbox_aci/policygroup_tab.html",
            context={
                "tab": self.tab,
                "object": intf,
                "ipg_table": ipg,
            },
        )
