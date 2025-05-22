"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import contract_filter_model
from .. forms import contract_filter_form

__all__ = (
    "ContractFilterView",
    "ContractFilterListView",
    "ContractFilterEditView",
    "ContractFilterDeleteView",
    "ContractFilterBulkDeleteView",
)


class ContractFilterView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = contract_filter_model.ContractFilter.objects.all()

    def get_extra_context(self, request, instance):

        filterentry = instance.entry_filter.all()
        filter_entry_table = tables.ContractFilterEntryTable(filterentry)

        return {
            'filter_entry_table': filter_entry_table,
            'related_models': self.get_related_models(request, instance),
        }


class ContractFilterListView(generic.ObjectListView):
    queryset = contract_filter_model.ContractFilter.objects.all()
    table = tables.ContractFilterTable


class ContractFilterEditView(generic.ObjectEditView):
    queryset = contract_filter_model.ContractFilter.objects.all()
    form = contract_filter_form.ContractFilterForm
    default_return_url = 'plugins:netbox_aci:contractfilter_list'


class ContractFilterDeleteView(generic.ObjectDeleteView):
    queryset = contract_filter_model.ContractFilter.objects.all()


class ContractFilterBulkDeleteView(generic.BulkDeleteView):
    queryset = contract_filter_model.ContractFilter.objects.all()
    table = tables.ContractFilterTable
