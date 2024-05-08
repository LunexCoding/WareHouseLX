from commands.center import g_commandCenter
from commands.consts import Constants, Commands
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
        COMMAND_TYPE = Constants.COMMAND_AUTHORIZATION
        commandID = Commands.getCommandByType(COMMAND_TYPE, None)
        response = g_commandCenter.execute(f"{commandID} {login} {password}")
        data = self._processingResponse(commandID, response)
        if data is None:
            _log.debug("User authorization failed.")
            return False
        self._userID = data[0]
        self._fullname = data[1]
        self._role = Roles.getRole(int(data[2]))
        _log.debug(f"User is authorized as <{self._fullname}> with UserID<{self._userID}>.")
        return True

    @staticmethod
    def _processingResponse(commandID, response):
        commandIDResponse = int(response.pop(0))
        commandStatus = int(response.pop(0))
        data = response.copy()
        if commandID == commandIDResponse and commandStatus == COMMAND_STATUS.EXECUTED:
            return data
        return None

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
