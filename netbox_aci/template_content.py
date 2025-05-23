from netbox.plugins import PluginTemplateExtension
#from . models import contract_model


class IpamVrfVzanyViewExtension(PluginTemplateExtension):
    models = ['ipam.vrf']

    def buttons(self):
        return self.render("netbox_aci/button_vzany.html")


class DcimInterfaceIpgViewExtension(PluginTemplateExtension):
    models = ['dcim.interface']

    def buttons(self):
        return self.render("netbox_aci/button_ipg.html")


#    def full_width_page(self):
#        obj = self.context['object']
#        consume_contracts = contract_model.Contract.objects.filter(vrfs_consume=obj)
#        provide_contracts = contract_model.Contract.objects.filter(vrfs_provide=obj)
#
#        return self.render("netbox_aci/netbox_ipam_vrf_vzanyviewextension.html",
#                           extra_context=
#                           {"vrf_consume_table": consume_contracts,
#                            "vrf_provide_table": provide_contracts,
#                            })

template_extensions = [IpamVrfVzanyViewExtension, DcimInterfaceIpgViewExtension]
