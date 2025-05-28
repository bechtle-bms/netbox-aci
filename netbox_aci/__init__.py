__version__ = '0.0.3'
__author__ = """Marc-Aurel Mohr-Lenné"""

from netbox.plugins import PluginConfig


class NetBoxAciConfig(PluginConfig):
    name = 'netbox_aci'
    verbose_name = 'NetBox ACI'
    description = 'Manage Cisco ACI in NetBox'
    version = __version__
    author = __author__
    base_url = 'aci'
    min_version = "4.1.3"
    max_version = "4.3.1"

config = NetBoxAciConfig
