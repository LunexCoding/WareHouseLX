from commands.center import g_commandCenter
from commands.status import COMMAND_STATUS
from commands.consts import Constants
from tools.tables import DatabaseTables


class _ReferenceBook:
    def __init__(self, table):
        self._table = table

    def loadRows(self):
        result = g_commandCenter.execute(Constants.LOAD_COMMAND.format(self._table))
        if result["Status"] == COMMAND_STATUS.EXECUTED:
            return result["Result"]
        return None

    def insertRow(self, data):
        columns = "[*]"
        values = ",".join(map(str, list(data.values())))
        command = Constants.ADD_COMMAND.format(self._table, columns, [values]).replace("'", "")
        result = g_commandCenter.execute(command)
        if result["Status"] == COMMAND_STATUS.EXECUTED:
            return result["Result"]
        return None

    @property
    def table(self):
        return self._table


g_bookIncomingDocuments = _ReferenceBook(DatabaseTables.INCOMING_DOCUMENTS)
