"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. import tables
from .. models import policy_link_level_model
from .. forms import policy_link_level_form

__all__ = (
    "LinkLevelView",
    "LinkLevelListView",
    "LinkLevelEditView",
    "LinkLevelDeleteView",
)


class LinkLevelView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = policy_link_level_model.LinkLevel.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class LinkLevelListView(generic.ObjectListView):
    queryset = policy_link_level_model.LinkLevel.objects.all()
    table = tables.LinkLevelTable


class LinkLevelEditView(generic.ObjectEditView):
    queryset = policy_link_level_model.LinkLevel.objects.all()
    form = policy_link_level_form.LinkLevelForm
    default_return_url = 'plugins:netbox_aci:linklevel_list'


class LinkLevelDeleteView(generic.ObjectDeleteView):
    queryset = policy_link_level_model.LinkLevel.objects.all()
