from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

ap_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_aci:applicationprofile_list',
        link_text='Application Profiles',
        permissions=['netbox_aci.view_applicationprofile'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:applicationprofile_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_applicationprofile'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_aci:endpointgroup_list',
        link_text='Application EPGs',
        permissions=['netbox_aci.view_endpointgroup'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:endpointgroup_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_endpointgroup'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_aci:endpointsecuritygroup_list',
        link_text='Endpoint Security Groups',
        permissions=['netbox_aci.view_endpointsecuritygroup'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:endpointsecuritygroup_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_endpointsecuritygroup'],
            ),
        ),
    ),
)

contract_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_aci:contract_list',
        link_text='Standard',
        permissions=['netbox_aci.view_contract'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:contract_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_contract'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_aci:contractfilter_list',
        link_text='Filters',
        permissions=['netbox_aci.view_contract'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:contractfilter_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_contract'],
            ),
        ),
    ),
)

nwtworking_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_aci:bridgedomain_list',
        link_text='Bridge Domains',
        permissions=['netbox_aci.view_bridgedomain'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:bridgedomain_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_bridgedomain'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_aci:l3out_list',
        link_text='L3Outs',
        permissions=['netbox_aci.view_l3out'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:l3out_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_l3out'],
            ),
        ),
    ),
)

fabric_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_aci:domain_list',
        link_text='Domains',
        permissions=['netbox_aci.view_domain'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:domain_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_domain'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_aci:aaep_list',
        link_text='Attachable Access Entity Profiles',
        permissions=['netbox_aci.view_aaep'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:aaep_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_aaep'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_aci:policygroup_list',
        link_text='Policy Groups',
        permissions=['netbox_aci.view_policygroup'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:policygroup_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_policygroup'],
            ),
        ),
    ),
)

policy_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_aci:linklevel_list',
        link_text='Link Levels',
        permissions=['netbox_aci.view_linklevel'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_aci:linklevel_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_aci.add_linklevel'],
            ),
        ),
    ),
)

menu = PluginMenu(
    label = 'ACI',
    groups=(("Application Profiles", ap_menu_items),
            ("Contracts", contract_menu_items),
            ("Networking", nwtworking_menu_items),
            ("Fabric", fabric_menu_items),
            ("Policies", policy_menu_items),
            ),
    icon_class='mdi mdi-router'
)
