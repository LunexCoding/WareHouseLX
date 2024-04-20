from commands.status import COMMAND_STATUS


class Client:
    def __init__(self, socket, addr):
        self._socket = socket
        self._addr = addr
        self._userID = None
        self.isAuthorized = False
        self._fullname = None

    def authorization(self, data):
        if data["Status"] == COMMAND_STATUS.EXECUTED:
            self._userID = data["Result"]["ID"]
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
