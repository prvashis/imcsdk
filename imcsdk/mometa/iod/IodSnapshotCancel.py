"""This module contains the general information for IodSnapshotCancel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IodSnapshotCancelConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"


class IodSnapshotCancel(ManagedObject):
    """This is IodSnapshotCancel class."""

    consts = IodSnapshotCancelConsts()
    naming_props = set([])

    mo_meta = MoMeta("IodSnapshotCancel", "iodSnapshotCancel", "snapshotCancel", VersionMeta.Version152, "InputOutput", 0x3f, [], ["admin"], [u'iodController'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version152, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["30-240"]), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "timeOut": "time_out", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.status = None
        self.time_out = None

        ManagedObject.__init__(self, "IodSnapshotCancel", parent_mo_or_dn, **kwargs)

