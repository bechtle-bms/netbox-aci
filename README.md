# Netbox ACI Plugin
A [Netbox](https://github.com/netbox-community/netbox) plugin for [Cisco ACI](https://www.cisco.com/site/de/de/products/networking/cloud-networking/application-centric-infrastructure/index.html) related objects in Netbox.

## Features

This plugin provides the following models to be able to document an Cisco ACI setup:

- Attachable Access Entity Profiles
- Application Profiles
- Bridge Domains
- Contracts (Standard)
- Endpoint Groups
- Endpoint Security Groups
- Interface Policy Groups
- L3 Outs
- Link Level Policies

## Contributing

This project is currently maintained jointly by:

- [Marc-Aurel Mohr-Lenné](https://github.com/bechtle-bms)

## Compatibility

Below listed plugin Versions has been tested with its corresponding NetBox Version.

|Netbox       |Plugin     |
|-------------|-----------|
| 4.1.3       | >= 0.0.1  |
| 4.2.0       | >= 0.0.1  |
| 4.3.1       | >= 0.0.2  |

## Installation

### Option 1
Install using [Docker](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins)<br>
Enable the plugin in `<netbox docker>/configuration/plugins.py`.

### Option 2
```
$ python3 -m pip install netbox-aci
```
Enable the plugin in `<netbox>/configuration.py`.

```
PLUGINS = [
    "netbox_aci"
]
```

## Requirements

* Custom Field:

        - name: "gateway"
          label: "Gateway"
          object_types:
            - "ipam.ipaddress"
          required: false
          type: "boolean"
          default: false

* Fixtures:

        You can load the requirements manually:
        python3 manage.py loaddata defaults.json

        !!! NOTE AND ADJUST THE VALUES FOR pk AND object_types BEFOREHAND !!!
        ipam.ipaddress value must be an integer.

        Example to get the integer value for ipam.ipaddress:
            python3 manage.py shell
            from django.contrib.contenttypes.models import ContentType
            from ipam.models.ip import IPAddress
            model_id = ContentType.objects.get_for_model(IPAddress)
            print(model_id.id)
            exit()
