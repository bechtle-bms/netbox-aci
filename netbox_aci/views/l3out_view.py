"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import l3out_model
from .. forms import l3out_form

__all__ = (
    "L3OutView",
    "L3OutListView",
    "L3OutEditView",
    "L3OutDeleteView",
    "L3OutBulkDeleteView",
)


class L3OutView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = l3out_model.L3Out.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'domain_table': instance.domains.all(),
            'vrf': instance.vrf,
            'related_models': self.get_related_models(request, instance),
        }


class L3OutListView(generic.ObjectListView):
    queryset = l3out_model.L3Out.objects.all()
    table = tables.L3OutTable


class L3OutEditView(generic.ObjectEditView):
    queryset = l3out_model.L3Out.objects.all()
    form = l3out_form.L3OutForm
    default_return_url = 'plugins:netbox_aci:l3out_list'


class L3OutDeleteView(generic.ObjectDeleteView):
    queryset = l3out_model.L3Out.objects.all()


class L3OutBulkDeleteView(generic.BulkDeleteView):
    queryset = l3out_model.L3Out.objects.all()
    table = tables.L3OutTable
