"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin

from .. tables import policies_tables
from .. models import policies_model
from .. forms import policies_form

__all__ = (
    "LinkLevelView",
    "LinkLevelListView",
    "LinkLevelEditView",
    "LinkLevelDeleteView",
    "CDPView",
    "CDPListView",
    "CDPEditView",
    "CDPDeleteView",
    "LLDPView",
    "LLDPListView",
    "LLDPEditView",
    "LLDPDeleteView",
    "PortChannelView",
    "PortChannelListView",
    "PortChannelEditView",
    "PortChannelDeleteView",
)


class LinkLevelView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = policies_model.LinkLevel.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class LinkLevelListView(generic.ObjectListView):
    queryset = policies_model.LinkLevel.objects.all()
    table = policies_tables.LinkLevelTable


class LinkLevelEditView(generic.ObjectEditView):
    queryset = policies_model.LinkLevel.objects.all()
    form = policies_form.LinkLevelForm
    default_return_url = 'plugins:netbox_aci:linklevel_list'


class LinkLevelDeleteView(generic.ObjectDeleteView):
    queryset = policies_model.LinkLevel.objects.all()


class CDPView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = policies_model.CDP.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class CDPListView(generic.ObjectListView):
    queryset = policies_model.CDP.objects.all()
    table = policies_tables.CDPTable


class CDPEditView(generic.ObjectEditView):
    queryset = policies_model.CDP.objects.all()
    form = policies_form.CDPForm
    default_return_url = 'plugins:netbox_aci:cdp_list'


class CDPDeleteView(generic.ObjectDeleteView):
    queryset = policies_model.CDP.objects.all()


class LLDPView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = policies_model.LLDP.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class LLDPListView(generic.ObjectListView):
    queryset = policies_model.LLDP.objects.all()
    table = policies_tables.LLDPTable


class LLDPEditView(generic.ObjectEditView):
    queryset = policies_model.LLDP.objects.all()
    form = policies_form.LLDPForm
    default_return_url = 'plugins:netbox_aci:lldp_list'


class LLDPDeleteView(generic.ObjectDeleteView):
    queryset = policies_model.LLDP.objects.all()


class PortChannelView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = policies_model.PortChannel.objects.all()

    def get_extra_context(self, request, instance):

        return {
            'related_models': self.get_related_models(request, instance),
        }


class PortChannelListView(generic.ObjectListView):
    queryset = policies_model.PortChannel.objects.all()
    table = policies_tables.PortChannelTable


class PortChannelEditView(generic.ObjectEditView):
    queryset = policies_model.PortChannel.objects.all()
    form = policies_form.PortChannelForm
    default_return_url = 'plugins:netbox_aci:portchannel_list'


class PortChannelDeleteView(generic.ObjectDeleteView):
    queryset = policies_model.PortChannel.objects.all()
