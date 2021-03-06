"""This module contains the general information for AdaptorFcPortPLogiProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcPortPLogiProfileConsts:
    pass


class AdaptorFcPortPLogiProfile(ManagedObject):
    """This is AdaptorFcPortPLogiProfile class."""

    consts = AdaptorFcPortPLogiProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcPortPLogiProfile", "adaptorFcPortPLogiProfile", "fc-port-plogi", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'adaptorHostFcIf'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1000-255000"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "retries": "retries", 
        "rn": "rn", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.retries = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AdaptorFcPortPLogiProfile", parent_mo_or_dn, **kwargs)

