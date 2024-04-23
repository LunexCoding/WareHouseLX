from commands.status import COMMAND_STATUS
from commands.accessLevel import ROLES


class Client:
    def __init__(self, socket, addr):
        self._socket = socket
        self._addr = addr
        self._userID = None
        self._role = ROLES.GUEST
        self.isAuthorized = False
        self._fullname = None

    def authorization(self, data):
        if data["Status"] == COMMAND_STATUS.EXECUTED:
            self._userID = data["Result"]["ID"]
            self._role = ROLES.getRoleStatus(data["Result"]["Role"])
            self._fullname = data["Result"]["Fullname"]
            self.isAuthorized = True
            return True
        return False

    @property
    def socket(self):
        return self._socket

    @property
    def addr(self):
        return self._addr

    @property
    def userID(self):
        return self._userID

    @property
    def fullname(self):
        return self._fullname

    @property
    def role(self):
        return self._role
