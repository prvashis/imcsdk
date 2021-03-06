"""This module contains the general information for IodSnapshotStart ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IodSnapshotStartConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    ISO_SHARE_TYPE_CIFS = "cifs"
    ISO_SHARE_TYPE_NFS = "nfs"
    ISO_SHARE_TYPE_SD = "sd"
    ISO_SHARE_TYPE_WWW = "www"
    REMOTE_SHARE_TYPE_SCP = "scp"
    REMOTE_SHARE_TYPE_SFTP = "sftp"
    REMOTE_SHARE_TYPE_TFTP = "tftp"


class IodSnapshotStart(ManagedObject):
    """This is IodSnapshotStart class."""

    consts = IodSnapshotStartConsts()
    naming_props = set([])

    mo_meta = MoMeta("IodSnapshotStart", "iodSnapshotStart", "snapshotStart", VersionMeta.Version152, "InputOutput", 0x1ffff, [], ["admin"], [u'iodController'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version152, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "iso_share": MoPropertyMeta("iso_share", "isoShare", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []), 
        "iso_share_file": MoPropertyMeta("iso_share_file", "isoShareFile", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "iso_share_ip": MoPropertyMeta("iso_share_ip", "isoShareIp", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []), 
        "iso_share_path": MoPropertyMeta("iso_share_path", "isoSharePath", "string", VersionMeta.Version152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "iso_share_type": MoPropertyMeta("iso_share_type", "isoShareType", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["cifs", "nfs", "sd", "www"], []), 
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []), 
        "remote_share_password": MoPropertyMeta("remote_share_password", "remoteSharePassword", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []), 
        "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
        "remote_share_type": MoPropertyMeta("remote_share_type", "remoteShareType", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["scp", "sftp", "tftp"], []), 
        "remote_share_username": MoPropertyMeta("remote_share_username", "remoteShareUsername", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["30-240"]), 
        "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "isoShare": "iso_share", 
        "isoShareFile": "iso_share_file", 
        "isoShareIp": "iso_share_ip", 
        "isoSharePath": "iso_share_path", 
        "isoShareType": "iso_share_type", 
        "password": "password", 
        "remoteShareFile": "remote_share_file", 
        "remoteShareIp": "remote_share_ip", 
        "remoteSharePassword": "remote_share_password", 
        "remoteSharePath": "remote_share_path", 
        "remoteShareType": "remote_share_type", 
        "remoteShareUsername": "remote_share_username", 
        "rn": "rn", 
        "status": "status", 
        "timeOut": "time_out", 
        "username": "username", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.iso_share = None
        self.iso_share_file = None
        self.iso_share_ip = None
        self.iso_share_path = None
        self.iso_share_type = None
        self.password = None
        self.remote_share_file = None
        self.remote_share_ip = None
        self.remote_share_password = None
        self.remote_share_path = None
        self.remote_share_type = None
        self.remote_share_username = None
        self.status = None
        self.time_out = None
        self.username = None

        ManagedObject.__init__(self, "IodSnapshotStart", parent_mo_or_dn, **kwargs)

