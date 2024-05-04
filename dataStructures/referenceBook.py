from commands.center import g_commandCenter
from commands.status import COMMAND_STATUS
from commands.consts import Constants
from tools.tables import DatabaseTables


class _ReferenceBook:
    def __init__(self, table):
        self._table = table
        self._rows = []

    def loadRows(self):
        result = g_commandCenter.execute(Constants.LOAD_COMMAND.format(self._table))
        if result["Status"] == COMMAND_STATUS.EXECUTED:
            if result["Result"] is not None:
                for row in result["Result"]:
                    self._rows.append(row)
                return result["Result"]
            return None

    def insertRow(self, data):
        del data["ID"]
        del data["ContractNumber"]
        columns = "[*]"
        values = ",".join(map(str, list(data.values())))
        command = Constants.ADD_COMMAND.format(self._table, columns, [values]).replace("'", "")
        result = g_commandCenter.execute(command)
        if result["Status"] == COMMAND_STATUS.EXECUTED:
            self._rows.append(result["Result"])
            return result["Result"]
        return None

    @property
    def table(self):
        return self._table

    @property
    def rows(self):
        return self._rows


g_bookIncomingDocuments = _ReferenceBook(DatabaseTables.INCOMING_DOCUMENTS)
