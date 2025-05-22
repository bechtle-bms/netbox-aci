"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import epg_model
from .. forms import epg_form
from .. import filtersets

__all__ = (
    "EndPointGroupView",
    "EndPointGroupListView",
    "EndPointGroupEditView",
    "EndPointGroupDeleteView",
    "EndPointGroupBulkDeleteView",
)


class EndPointGroupView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = epg_model.EndPointGroup.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'domain_table': instance.domains.all(),
            'contract_consume_table': instance.contracts_consume.all(),
            'contract_provide_table': instance.contracts_provide.all(),
            'subnet_table': instance.subnets.all(),
            'related_models': self.get_related_models(request, instance),
        }


class EndPointGroupListView(generic.ObjectListView):
    queryset = epg_model.EndPointGroup.objects.all()
    table = tables.EndPointGroupTable
    filterset = filtersets.EndPointGroupListFilterSet
    filterset_form = epg_form.EndPointGroupFilterForm


class EndPointGroupEditView(generic.ObjectEditView):
    queryset = epg_model.EndPointGroup.objects.all()
    form = epg_form.EndPointGroupForm
    default_return_url = 'plugins:netbox_aci:endpointgroup_list'


class EndPointGroupDeleteView(generic.ObjectDeleteView):
    queryset = epg_model.EndPointGroup.objects.all()


class EndPointGroupBulkDeleteView(generic.BulkDeleteView):
    queryset = epg_model.EndPointGroup.objects.all()
    table = tables.EndPointGroupTable
