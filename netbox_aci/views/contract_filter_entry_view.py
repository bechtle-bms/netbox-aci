"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import contract_filter_entry_model
from .. forms import contract_filter_entry_form

__all__ = (
    "ContractFilterEntryView",
    "ContractFilterEntryListView",
    "ContractFilterEntryEditView",
    "ContractFilterEntryDeleteView",
    "ContractFilterEntryBulkDeleteView",
)


class ContractFilterEntryView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = contract_filter_entry_model.ContractFilterEntry.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class ContractFilterEntryListView(generic.ObjectListView):
    queryset = contract_filter_entry_model.ContractFilterEntry.objects.all()
    table = tables.ContractFilterEntryTable


class ContractFilterEntryEditView(generic.ObjectEditView):
    queryset = contract_filter_entry_model.ContractFilterEntry.objects.all()
    form = contract_filter_entry_form.ContractFilterEntryForm
    default_return_url = 'plugins:netbox_aci:contractfilterentry_list'


class ContractFilterEntryDeleteView(generic.ObjectDeleteView):
    queryset = contract_filter_entry_model.ContractFilterEntry.objects.all()

class ContractFilterEntryBulkDeleteView(generic.BulkDeleteView):
    queryset = contract_filter_entry_model.ContractFilterEntry.objects.all()
    table = tables.ContractFilterEntryTable
