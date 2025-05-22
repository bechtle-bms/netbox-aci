"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import aaep_model
from .. forms import aaep_form
from .. import filtersets

__all__ = (
    "AAEPView",
    "AAEPListView",
    "AAEPEditView",
    "AAEPDeleteView",
    "AAEPBulkDeleteView",
    "AAEPStaticBindingView",
    "AAEPStaticBindingListView",
    "AAEPStaticBindingEditView",
    "AAEPStaticBindingDeleteView",
    "AAEPStaticBindingBulkDeleteView",
)


class AAEPView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = aaep_model.AAEP.objects.all()

    def get_extra_context(self, request, instance):

        aaepstatic = instance.aaepstaticbinding_aaep.all()
        static_table = tables.AAEPStaticBindingTable(aaepstatic)
        return {
            'domain_table': instance.domains.all(),
            'static_table': static_table,
            'related_models': self.get_related_models(request, instance),
        }


class AAEPListView(generic.ObjectListView):
    queryset = aaep_model.AAEP.objects.all()
    table = tables.AAEPTable
    filterset = filtersets.AAEPListFilterSet
    filterset_form = aaep_form.AAEPFilterForm

class AAEPEditView(generic.ObjectEditView):
    queryset = aaep_model.AAEP.objects.all()
    form = aaep_form.AAEPForm
    default_return_url = 'plugins:netbox_aci:aaep_list'


class AAEPDeleteView(generic.ObjectDeleteView):
    queryset = aaep_model.AAEP.objects.all()


class AAEPBulkDeleteView(generic.BulkDeleteView):
    queryset = aaep_model.AAEP.objects.all()
    table = tables.AAEPTable


# Static Binding

class AAEPStaticBindingView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = aaep_model.AAEPStaticBinding.objects.all()


class AAEPStaticBindingListView(generic.ObjectListView):
    queryset = aaep_model.AAEPStaticBinding.objects.all()
    table = tables.AAEPStaticBindingTable
    actions = {'add': {'add'}}


class AAEPStaticBindingEditView(generic.ObjectEditView):
    queryset = aaep_model.AAEPStaticBinding.objects.all()
    form = aaep_form.AAEPStaticBindingForm
    default_return_url = 'plugins:netbox_aci:aaepstaticbinding_list'


class AAEPStaticBindingDeleteView(generic.ObjectDeleteView):
    queryset = aaep_model.AAEPStaticBinding.objects.all()


class AAEPStaticBindingBulkDeleteView(generic.BulkDeleteView):
    queryset = aaep_model.AAEPStaticBinding.objects.all()
    table = tables.AAEPStaticBindingTable
