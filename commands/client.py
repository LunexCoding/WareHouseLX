from .consts import Constants
from .status import COMMAND_STATUS
from .command import BaseCommand, VALUE_TYPE
from .accessLevel import ACCESS_LEVEL, ROLES
from .processСonditions import ProcessConditions
from dataStructures.referenceBook import g_referenceBooks
from tools.logger import logger
from tools.dateConverter import convertTimestampToDate, convertDateToTimestamp


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
    COMMAND_NAME = Constants.COMMAND_SEARCH

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
    COMMAND_NAME = Constants.COMMAND_ADD

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-c": VALUE_TYPE.LIST,
            "-v": VALUE_TYPE.LIST,
            "-t": VALUE_TYPE.STRING
        }
        self._argsWithoutFlagsOrder = ["-c", "-v", "-t"]
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.USER

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:

                table = args["-t"]
                referenceBook = [book for book in g_referenceBooks if book.table == table][0]
                columns = args["-c"]
                if len(columns) == 1 and columns[0] == "*":
                    columns = referenceBook.columnsForInsertion.copy()
                values = args["-v"]

                row = dict(zip(columns, values))
                row["CreationDate"] = convertTimestampToDate(row["CreationDate"])
                rowID = referenceBook.addRow(row)
                if rowID is not None:
                    status, result = SearchRows().execute(client, f"{table} ID={rowID}")
                    if status == COMMAND_STATUS.EXECUTED:
                        result["CreationDate"] = convertDateToTimestamp(result["CreationDate"])
                        return COMMAND_STATUS.EXECUTED, [result]

                    return COMMAND_STATUS.FAILED, None
                return COMMAND_STATUS.FAILED, None
            return executionPermission

        return COMMAND_STATUS.FAILED, None


class Authorization(ClientCommand):
    COMMAND_NAME = Constants.COMMAND_AUTHORIZATION

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
                    return COMMAND_STATUS.EXECUTED, [user]

                return COMMAND_STATUS.FAILED, Constants.USER_NOT_FOUND
            return executionPermission

        return COMMAND_STATUS.FAILED, Constants.AUTHORIZATION_COMMAND_FAILED

    @staticmethod
    def _getUser(login, password, referenceBook):
        condition = f"Login='{login}'|Password='{password}'"
        processedCondition = ProcessConditions.process(condition.split("|"), referenceBook.columns)
        user = referenceBook.searchRowByParams(processedCondition)
        if user:
            return user
        return None

    @staticmethod
    def _getRole(user):
        referenceBook = [book for book in g_referenceBooks if book.table == Constants.TABLE_ROLES][0]
        roleID = user['RoleID']
        condition = f"ID={roleID}"
        processedCondition = ProcessConditions.process(condition.split("|"), referenceBook.columns)
        role = referenceBook.searchRowByParams(processedCondition)["Name"]
        return role


class LoadRows(ClientCommand):
    COMMAND_NAME = Constants.COMMAND_LOAD

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": VALUE_TYPE.STRING
        }
        self._argsWithoutFlagsOrder = ["-t"]
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.USER

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:

                table = args["-t"]
                referenceBook = [book for book in g_referenceBooks if book.table == table][0]
                rows = referenceBook.loadRows(client)
                return COMMAND_STATUS.EXECUTED, rows

            return executionPermission
        return COMMAND_STATUS.FAILED, Constants.AUTHORIZATION_COMMAND_FAILED


class DeleteRow(ClientCommand):
    COMMAND_NAME = Constants.COMMAND_DELETE

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-i": VALUE_TYPE.INT,
            "-t": VALUE_TYPE.STRING
        }
        self._argsWithoutFlagsOrder = ["-i", "-t"]
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.ADMIN

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:

                rowID = args["-i"]
                table = args["-t"]
                referenceBook = [book for book in g_referenceBooks if book.table == table][0]
                referenceBook.deleteRow(rowID)
                return COMMAND_STATUS.EXECUTED, rowID

            return executionPermission
        return COMMAND_STATUS.FAILED, Constants.AUTHORIZATION_COMMAND_FAILED


class UpdateRow(ClientCommand):
    COMMAND_NAME = Constants.COMMAND_UPDATE

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": VALUE_TYPE.STRING,
            "-c": VALUE_TYPE.LIST,
            "-v": VALUE_TYPE.LIST
        }
        self._argsWithoutFlagsOrder = ["-c", "-v", "-t"]
        self.isAuthorizedLevel = True
        self.requiredAccessLevel = ACCESS_LEVEL.ADMIN

    def execute(self, client=None, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            executionPermission = self._checkExecutionPermission(client)
            if executionPermission[0] == COMMAND_STATUS.EXECUTED:
                table = args["-t"]
                columns = args["-c"]
                values = [value.replace(Constants.SERVICE_SYMBOL_FOR_ARGS, " ") for value in args["-v"]]
                data = dict(zip(columns, values))
                rowID = data["ID"]
                del data["ID"]
                referenceBook = [book for book in g_referenceBooks if book.table == table][0]
                row = referenceBook.updateRow(rowID, data)
                return COMMAND_STATUS.EXECUTED, [row]

            return executionPermission
        return COMMAND_STATUS.FAILED, Constants.AUTHORIZATION_COMMAND_FAILED


COMMANDS = {
    SearchRows.COMMAND_NAME: SearchRows,
    AddRow.COMMAND_NAME: AddRow,
    LoadRows.COMMAND_NAME: LoadRows,
    DeleteRow.COMMAND_NAME: DeleteRow,
    UpdateRow.COMMAND_NAME: UpdateRow,
    Authorization.COMMAND_NAME: Authorization
}
