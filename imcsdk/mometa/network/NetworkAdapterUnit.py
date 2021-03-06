"""This module contains the general information for NetworkAdapterUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class NetworkAdapterUnitConsts:
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_MISSING = "missing"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNKNOWN = "unknown"


class NetworkAdapterUnit(ManagedObject):
    """This is NetworkAdapterUnit class."""

    consts = NetworkAdapterUnitConsts()
    naming_props = set([u'slot'])

    mo_meta = MoMeta("NetworkAdapterUnit", "networkAdapterUnit", "network-adapter-[slot]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'computeRackUnit'], [u'networkAdapterEthIf'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_intf": MoPropertyMeta("num_intf", "numIntf", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "missing", "not-supported", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "numIntf": "num_intf", 
        "presence": "presence", 
        "rn": "rn", 
        "slot": "slot", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot, **kwargs):
        self._dirty_mask = 0
        self.slot = slot
        self.child_action = None
        self.model = None
        self.num_intf = None
        self.presence = None
        self.status = None

        ManagedObject.__init__(self, "NetworkAdapterUnit", parent_mo_or_dn, **kwargs)

