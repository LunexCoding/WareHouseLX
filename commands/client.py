import time

from .consts import Constants
from .status import COMMAND_STATUS
from .command import BaseCommand, ValueType
from .processСonditions import ProcessConditions
from dataStructures.referenceBook import g_referenceBooks


class ClientCommand(BaseCommand):
    def __init__(self):
        super().__init__()
        self.isAuthorizedLevel = False


class SearchRows(ClientCommand):
    COMMAND_NAME = "search"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": ValueType.STRING,
            "-c": ValueType.STRING
        }
        self._argsWithoutFlagsOrder = ["-t", "-c"]
        self.isAuthorizedLevel = True

    def execute(self, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            table = args["-t"]
            referenceBook = [book for book in g_referenceBooks if book.table == table][0]
            conditionString = args["-c"]

            conditions = ProcessConditions.process(conditionString.split("|"), referenceBook.columns)
            data = referenceBook.searchRowByParams(conditions)
            return COMMAND_STATUS.EXECUTED, data
        return COMMAND_STATUS.FAILED, None


class AddRow(ClientCommand):
    COMMAND_NAME = "add"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": ValueType.STRING,
            "-c": ValueType.LIST,
            "-v": ValueType.LIST
        }
        self._argsWithoutFlagsOrder = ["-t", "-c", "-v"]
        self.isAuthorizedLevel = True

    def execute(self, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

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


class Authorization(ClientCommand):
    COMMAND_NAME = "authorization"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-l": ValueType.STRING,
            "-p": ValueType.STRING
        }
        self._argsWithoutFlagsOrder = ["-l", "-p"]
        self.isAuthorizedLevel = False

    def execute(self, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            referenceBook = [book for book in g_referenceBooks if book.table == Constants.TABLE_FOR_AUTHORZATION][0]
            login = args["-l"]
            password = args["-p"]

            user = self._getUser(login, password, referenceBook)
            if user is not None:
                role = self._getRole(user)
                user["Role"] = role
                del user["Login"]
                del user["Password"]
                del user["RoleID"]
                return COMMAND_STATUS.EXECUTED, user
            return COMMAND_STATUS.FAILED, Constants.USER_NOT_FOUND
        return COMMAND_STATUS.FAILED, Constants.AUTHORIZATION_COMMAND_FAILED

    @staticmethod
    def _getUser(login, password, referenceBook):
        condition = f"Login='{login}'|Password='{password}'"
        processedCondition = ProcessConditions.process(condition.split("|"), referenceBook.columns)
        user = referenceBook.searchRowByParams(processedCondition)[0]
        if user:
            return user
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

    def execute(self, commandArgs=None):
        # Имитация долгой работы на 10 секунд
        start_time = time.time()
        while time.time() - start_time < 10:
            pass
        return COMMAND_STATUS.EXECUTED, None


COMMANDS = {
    SearchRows.COMMAND_NAME: SearchRows,
    AddRow.COMMAND_NAME: AddRow,
    LongRunningCommand.COMMAND_NAME: LongRunningCommand,
    Authorization.COMMAND_NAME: Authorization
}
