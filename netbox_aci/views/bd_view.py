"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import bd_model
from .. forms import bd_form
from .. import filtersets

__all__ = (
    "BridgeDomainView",
    "BridgeDomainListView",
    "BridgeDomainEditView",
    "BridgeDomainDeleteView",
    "BridgeDomainBulkDeleteView",
)


class BridgeDomainView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = bd_model.BridgeDomain.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'vrf': instance.vrf,
            'subnet_table': instance.subnets.all(),
            'l3out_table': instance.l3outs.all(),
            'related_models': self.get_related_models(request, instance),
        }


class BridgeDomainListView(generic.ObjectListView):
    queryset = bd_model.BridgeDomain.objects.all()
    table = tables.BridgeDomainTable
    filterset = filtersets.BridgeDomainListFilterSet
    filterset_form = bd_form.BridgeDomainFilterForm


class BridgeDomainEditView(generic.ObjectEditView):
    queryset = bd_model.BridgeDomain.objects.all()
    form = bd_form.BridgeDomainForm
    default_return_url = 'plugins:netbox_aci:bridgedomain_list'


class BridgeDomainDeleteView(generic.ObjectDeleteView):
    queryset = bd_model.BridgeDomain.objects.all()


class BridgeDomainBulkDeleteView(generic.BulkDeleteView):
    queryset = bd_model.BridgeDomain.objects.all()
    table = tables.BridgeDomainTable
