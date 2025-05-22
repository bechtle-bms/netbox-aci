"""
Choice sets used by the models, views and forms.
"""

from utilities.choices import ChoiceSet

__all__ = (
    "BridgeDomainL2UUCChoices",
    "ContractScopeChoices",
    "ContractQoSClassChoices",
    "ContractTargetDSCPChoices",
    "ContractFilterACtionChoices",
    "ContractFilterEntryEtherTypeChoices",
    "ContractFilterDirectivesChoices",
    "ContractFilterEntryARPFlagChoices",
    "ContractFilterEntryIPProtocolChoices",
    "DomainTypeChoices",
    "PoolAllocationModeChoices",
    "AAEPStaticBindingModeChoices",
    "LinkLevelNegotiationChoices",
    "LinkLevelSpeedChoices",
)


class BridgeDomainL2UUCChoices(ChoiceSet):
    """
    Defines the choices availble for the L2 Unknown Unicast.
    """

    FLOOD = "flood"
    HARDWARE_PROXY = "hardware_proxy"

    CHOICES = [
        ('', "----"),
        (FLOOD, "flood"),
        (HARDWARE_PROXY, "hardware_proxy"),
    ]


class ContractScopeChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract scope.
    """

    SCOPE_VRF = "vrf"
    SCOPE_TENANT = "tenant"
    SCOPE_GLOBAL = "global"

    CHOICES = [
        ('', "----"),
        (SCOPE_VRF, "vrf"),
        (SCOPE_TENANT, "tenant"),
        (SCOPE_GLOBAL, "global"),
    ]


class ContractQoSClassChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Qos Class.
    """

    LEVEL1 = "level1"
    LEVEL2 = "level2"
    LEVEL3 = "level3"
    LEVEL4 = "level4"
    LEVEL5 = "level5"
    LEVEL6 = "level6"

    CHOICES = [
        ('', "----"),
        (LEVEL1, "level1"),
        (LEVEL2, "level2"),
        (LEVEL3, "level3"),
        (LEVEL4, "level4"),
        (LEVEL5, "level5"),
        (LEVEL6, "level6"),
    ]


class ContractTargetDSCPChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Target DSCP.
    """

    AF11 = "af11"
    AF12 = "af12"
    AF13 = "af13"
    AF21 = "af21"
    AF22 = "af22"
    AF23 = "af23"
    AF31 = "af31"
    AF32 = "af32"
    AF33 = "af33"
    AF41 = "af41"
    AF42 = "af42"
    AF43 = "af43"
    CS0 = "cs0"
    CS1 = "cs1"
    CS2 = "cs2"
    CS3 = "cs3"
    CS4 = "cs4"
    CS5 = "cs5"
    CS6 = "cs6"
    CS7 = "cs7"
    EXPEDITED_FORWARDING = "expedited_forwarding"
    VOICE_ADMIT = "voice_admit"

    CHOICES = [
        ('', "----"),
        (AF11, "af11"),
        (AF12, "af12"),
        (AF13, "af13"),
        (AF21, "af21"),
        (AF22, "af22"),
        (AF23, "af23"),
        (AF31, "af31"),
        (AF32, "af32"),
        (AF33, "af33"),
        (AF41, "af41"),
        (AF42, "af42"),
        (AF43, "af43"),
        (CS0, "cs0"),
        (CS1, "cs1"),
        (CS2, "cs2"),
        (CS3, "cs3"),
        (CS4, "cs4"),
        (CS5, "cs5"),
        (CS6, "cs6"),
        (CS7, "cs7"),
        (EXPEDITED_FORWARDING, "expedited_forwarding"),
        (VOICE_ADMIT, "voice_admit"),
    ]


class ContractFilterDirectivesChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Filter Directives.
    """

    LOG = "log"
    ENABLE_POLICY_COMPRESSION = "enable_policy_compression"

    CHOICES = [
        (LOG, "log"),
        (ENABLE_POLICY_COMPRESSION, "enable_policy_compression"),
    ]


class ContractFilterACtionChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Filter Action.
    """

    PERMIT = "permit"
    DENY = "deny"

    CHOICES = [
        ('', "----"),
        (PERMIT, "permit"),
        (DENY, "deny"),
    ]


class ContractFilterEntryEtherTypeChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Filter Entry EtherType.
    """

    IP = "ip"
    IPv4 = "ipv4"
    IPv6 = "ipv6"
    MPLS_UNICAST = "mpls_unicast"
    UNSPECIFIED = "unspecified"
    TRILL = "trill"
    ARP = "arp"
    FCOE = "fcoe"
    MAC_SECURITY = "mac_security"

    CHOICES = [
        ('', "----"),
        (IP, "ip"),
        (IPv4, "ipv4"),
        (IPv6, "ipv6"),
        (MPLS_UNICAST, "mpls_unicast"),
        (UNSPECIFIED, "unspecified"),
        (TRILL, "trill"),
        (ARP, "arp"),
        (FCOE, "fcoe"),
        (MAC_SECURITY, "mac_security"),
    ]


class ContractFilterEntryIPProtocolChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Filter Entry IP Protocol.
    """

    EIGRP = "eigrp"
    EGP = "egp"
    ICMP = "icmp"
    ICMPv6 = "icmpv6"
    IGMP = "igmp"
    IGP = "igp"
    L2TP = "l2tp"
    OSPF = "ospf"
    PIM = "pim"
    TCP = "tcp"
    UDP = "udp"
    UNSPECIFIED = "unspecified"

    CHOICES = [
        ('', "----"),
        (EIGRP, "eigrp"),
        (EGP, "egp"),
        (ICMP, "icmp"),
        (ICMPv6, "icmpv6"),
        (IGMP, "igmp"),
        (IGP, "igp"),
        (L2TP, "l2tp"),
        (OSPF, "ospf"),
        (PIM, "pim"),
        (TCP, "tcp"),
        (UDP, "udp"),
        (UNSPECIFIED, "unspecified"),
    ]


class ContractFilterEntryARPFlagChoices(ChoiceSet):
    """
    Defines the choices availble for the Contract Filter Entry ARP Flag.
    """

    ARP_REPLY = "reply"
    ARP_REQUEST = "request"
    UNSPECIFIED = "unspecified"

    CHOICES = [
        ('', "----"),
        (ARP_REPLY, "reply"),
        (ARP_REQUEST, "request"),
        (UNSPECIFIED, "unspecified"),
    ]


class DomainTypeChoices(ChoiceSet):
    """
    Defines the choices availble for the Domain Type.
    """

    PHYSICAL = "physical"
    VMM = "vmm"
    L3 = "l3"

    CHOICES = [
        ('', "----"),
        (PHYSICAL, "physical"),
        (VMM, "vmm"),
        (L3, "l3"),
    ]


class PoolAllocationModeChoices(ChoiceSet):
    """
    Defines the choices availble for the Pool Allocation Mode.
    """

    STATIC = "static"
    DYNAMIC = "dynamic"

    CHOICES = [
        ('', "----"),
        (STATIC, "static"),
        (DYNAMIC, "dynamic"),
    ]


class AAEPStaticBindingModeChoices(ChoiceSet):
    """
    Defines the choices availble for the static binding within an AAEP.
    """

    TRUNK = "trunk"
    ACCESS8021p = "access_8021p"
    ACCESSuntagged = "access_untagged"

    CHOICES = [
        ('', "----"),
        (TRUNK, "trunk"),
        (ACCESS8021p, "access_8021p"),
        (ACCESSuntagged, "access_untagged"),
    ]


class LinkLevelNegotiationChoices(ChoiceSet):
    """
    Defines the choices availble for an interface link level negotiation.
    """

    OFF = "off"
    ON = "on"
    ENFORCE = "enforce"

    CHOICES = [
        ('', "----"),
        (OFF, "off"),
        (ON, "on"),
        (ENFORCE, "enforce"),
    ]


class LinkLevelSpeedChoices(ChoiceSet):
    """
    Defines the choices availble for an interface link level speed.
    """

    INHERIT = "inherit"
    HUNDRED_MBPS = "100mbps"
    ONE_GBPS = "1gbps"
    TEN_GBPS = "10gbps"
    TWENTYFIVE_GBPS = "25gbps"
    FORTY_GBPS = "40gbps"
    HUNDRED_GBPS = "100gbps"
    FOURHUNDRET_GBPS = "400gbps"

    CHOICES = [
        ('', "----"),
        (INHERIT, "inherit"),
        (HUNDRED_MBPS, "100mbps"),
        (ONE_GBPS, "1gbps"),
        (TEN_GBPS, "10gbps"),
        (TWENTYFIVE_GBPS, "25gbps"),
        (FORTY_GBPS, "40gbps"),
        (HUNDRED_GBPS, "100gbps"),
        (FOURHUNDRET_GBPS, "400gbps"),
    ]
