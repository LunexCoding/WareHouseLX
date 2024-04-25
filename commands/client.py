import time

from .consts import Constants
from .status import COMMAND_STATUS
from .command import BaseCommand, VALUE_TYPE
from .accessLevel import ACCESS_LEVEL, ROLES
from .processСonditions import ProcessConditions
from dataStructures.referenceBook import g_referenceBooks
from tools.logger import logger


_log = logger.getLogger(__name__)


class ClientCommand(BaseCommand):
    def __init__(self):
        super().__init__()
        self.isAuthorizedLevel = False
        self.requiredAccessLevel = ACCESS_LEVEL.USER

    def _checkAccessLevel(self, clientRole):
        return True if clientRole >= self.requiredAccessLevel else False

    def _checkAuthorizedLevel(self, clientAuthorization):
        return True if clientAuthorization == self.isAuthorizedLevel else False

    def _checkExecutionPermission(self, client):
        if client is None:
            return COMMAND_STATUS.FAILED, Constants.CLIENT_NOT_ACCEPTED_MDG
        if not self._checkAccessLevel(client.role):
            return COMMAND_STATUS.FAILED, Constants.ACCESS_ERROR_MSG
        if not self._checkAuthorizedLevel(client.isAuthorized):
            return COMMAND_STATUS.FAILED, Constants.CLIENT_IS_NOT_AUTHORIZED_MSG
        return COMMAND_STATUS.EXECUTED, True


class SearchRows(ClientCommand):
    COMMAND_NAME = "search"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": VALUE_TYPE.STRING,
            "-c": VALUE_TYPE.STRING
        }
        self._argsWithoutFlagsOrder = ["-t", "-c"]
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.USER

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:

                table = args["-t"]
                referenceBook = [book for book in g_referenceBooks if book.table == table][0]
                conditionString = args["-c"]

                conditions = ProcessConditions.process(conditionString.split("|"), referenceBook.columns)
                data = referenceBook.searchRowByParams(conditions)
                return COMMAND_STATUS.EXECUTED, data
            return executionPermission

        return COMMAND_STATUS.FAILED, None


class AddRow(ClientCommand):
    COMMAND_NAME = "add"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": VALUE_TYPE.STRING,
            "-c": VALUE_TYPE.LIST,
            "-v": VALUE_TYPE.LIST
        }
        self._argsWithoutFlagsOrder = ["-t", "-c", "-v"]
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.ADMIN

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:

                table = args["-t"]
                referenceBook = [book for book in g_referenceBooks if book.table == table][0]
                columns = args["-c"]
                if len(columns) == 1 and columns[0] == "*":
                    columns = referenceBook.columns.copy()
                    del columns[0]
                values = args["-v"]

                try:
                    row = dict(zip(columns, values))
                    referenceBook.addRow(row)
                    return COMMAND_STATUS.EXECUTED, None
                except Exception:
                    return COMMAND_STATUS.FAILED, None
            return executionPermission

        return COMMAND_STATUS.FAILED, None


class Authorization(ClientCommand):
    COMMAND_NAME = "authorization"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-l": VALUE_TYPE.STRING,
            "-p": VALUE_TYPE.STRING
        }
        self._argsWithoutFlagsOrder = ["-l", "-p"]
        self.isAuthorizedLevel = False
        self.requiredAccessLevel = ACCESS_LEVEL.GUEST

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:

                referenceBook = [book for book in g_referenceBooks if book.table == Constants.TABLE_FOR_AUTHORZATION][0]
                login = args["-l"]
                password = args["-p"]

                user = self._getUser(login, password, referenceBook)
                if user is not None:
                    role = self._getRole(user)
                    user["Role"] = ROLES.getRoleStatus(role)
                    client.authorization(user)
                    del user["Login"]
                    del user["Password"]
                    del user["RoleID"]
                    _log.debug(f"Client is authorized -> ID<{user['ID']}>, fullname: {user['Fullname']}")
                    return COMMAND_STATUS.EXECUTED, user
                return COMMAND_STATUS.FAILED, Constants.USER_NOT_FOUND
            return executionPermission

        return COMMAND_STATUS.FAILED, Constants.AUTHORIZATION_COMMAND_FAILED

    @staticmethod
    def _getUser(login, password, referenceBook):
        condition = f"Login='{login}'|Password='{password}'"
        processedCondition = ProcessConditions.process(condition.split("|"), referenceBook.columns)
        user = referenceBook.searchRowByParams(processedCondition)
        if user:
            return user[0]
        return None

    @staticmethod
    def _getRole(user):
        referenceBook = [book for book in g_referenceBooks if book.table == Constants.TABLE_ROLES][0]
        roleID = user['RoleID']
        condition = f"ID={roleID}"
        processedCondition = ProcessConditions.process(condition.split("|"), referenceBook.columns)
        role = referenceBook.searchRowByParams(processedCondition)[0]["Name"]
        return role


class LongRunningCommand(ClientCommand):
    COMMAND_NAME = "long_run"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.USER

    def execute(self, client=None, commandArgs=None):
        # Имитация долгой работы на 10 секунд
        executionPermission = self._checkExecutionPermission(client)
        if executionPermission[0] == COMMAND_STATUS.EXECUTED:
            start_time = time.time()
            while time.time() - start_time < 10:
                pass
            return COMMAND_STATUS.EXECUTED, None
        return executionPermission


COMMANDS = {
    SearchRows.COMMAND_NAME: SearchRows,
    AddRow.COMMAND_NAME: AddRow,
    LongRunningCommand.COMMAND_NAME: LongRunningCommand,
    Authorization.COMMAND_NAME: Authorization
}
