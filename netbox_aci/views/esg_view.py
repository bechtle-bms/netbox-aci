"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import esg_model
from .. forms import esg_form
from .. import filtersets

__all__ = (
    "EndPointSecurityGroupView",
    "EndPointSecurityGroupListView",
    "EndPointSecurityGroupEditView",
    "EndPointSecurityGroupDeleteView",
    "EndPointSecurityGroupBulkDeleteView",
)


class EndPointSecurityGroupView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = esg_model.EndPointSecurityGroup.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'vrf': instance.vrf,
            'contract_provide_table': instance.contracts_provide.all(),
            'contract_consume_table': instance.contracts_consume.all(),
            'epg_selector_table': instance.epgs_selector.all(),
            'ip_subnet_selector_table': instance.ip_subnets_selector.all(),
            'tag_selector_table': instance.tags_selector.all(),
            'related_models': self.get_related_models(request, instance),
        }


class EndPointSecurityGroupListView(generic.ObjectListView):
    queryset = esg_model.EndPointSecurityGroup.objects.all()
    table = tables.EndPointSecurityGroupTable
    filterset = filtersets.EndPointSecurityGroupListFilterSet
    filterset_form = esg_form.EndPointSecurityGroupFilterForm

class EndPointSecurityGroupEditView(generic.ObjectEditView):
    queryset = esg_model.EndPointSecurityGroup.objects.all()
    form = esg_form.EndPointSecurityGroupForm
    default_return_url = 'plugins:netbox_aci:endpointsecuritygroup_list'


class EndPointSecurityGroupDeleteView(generic.ObjectDeleteView):
    queryset = esg_model.EndPointSecurityGroup.objects.all()


class EndPointSecurityGroupBulkDeleteView(generic.BulkDeleteView):
    queryset = esg_model.EndPointSecurityGroup.objects.all()
    table = tables.EndPointSecurityGroupTable
