from commands.center import g_commandCenter
from commands.consts import Constants
from commands.roles import Roles
from commands.status import COMMAND_STATUS
from tools.logger import logger


_log = logger.getLogger(__name__)


class _User:
    def __init__(self):
        self._userID = None
        self._login = None
        self._fullname = None
        self._role = Roles.getRole(0)

    def authorization(self, login, password):
        result = g_commandCenter.execute(Constants.AUTHORIZATION_COMMAND.format(login, password))
        if result["Status"] == COMMAND_STATUS.FAILED:
            _log.debug("User authorization failed.")
            return False
        self._userID = result["Result"]["ID"]
        self._fullname = result["Result"]["Fullname"]
        self._role = Roles.getRole(result["Result"]["Role"])
        _log.debug(f"User is authorized as <{self._fullname}> with UserID<{self._userID}>.")
        return True

    @property
    def userID(self):
        return self._userID

    @property
    def login(self):
        return self._login

    @property
    def fullname(self):
        return self._fullname

    @property
    def role(self):
        return self._role


g_user = _User()
