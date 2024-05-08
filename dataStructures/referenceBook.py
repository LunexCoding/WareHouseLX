from commands.center import g_commandCenter
from commands.consts import Constants, Commands
from commands.status import COMMAND_STATUS
from tools.dateConverter import convertTimestampToDate, isTimestamp
from tools.tables import DatabaseTables


class _ReferenceBook:
    def __init__(self, table):
        self._table = table
        self._rows = []

    @staticmethod
    def _processingResponse(commandID, response):
        commandIDResponse = int(response.pop(0))
        commandStatus = int(response.pop(0))
        if commandID == commandIDResponse and commandStatus == COMMAND_STATUS.EXECUTED:
            rowString = ' '.join(response)
            rows = rowString.split("|")
            for index, row in enumerate(rows):
                if row == "None":
                    return None
                rowData = []
                for value in row.split():
                    if isTimestamp(value):
                        rowData.append(convertTimestampToDate(value))
                    else:
                        rowData.append(value)
                rows[index] = rowData
            return rows
        return None

    def loadRows(self):
        COMMAND_TYPE = Constants.COMMAND_LOAD
        commandID = Commands.getCommandByType(COMMAND_TYPE, dict(table=self._table))
        response = g_commandCenter.execute(commandID)
        data = self._processingResponse(commandID, response)
        if data is not None:
            for row in data:
                if row not in self._rows:
                    self._rows.append(row)
                    return data
        return None

    def insertRow(self, data):
        COMMAND_TYPE = Constants.COMMAND_ADD
        commandID = Commands.getCommandByType(COMMAND_TYPE, dict(table=self._table))
        columns = "[*]"
        values = ",".join(map(str, list(data.values())))
        command = "{} {} {}".format(commandID, columns, [values]).replace("'", "")
        response = g_commandCenter.execute(command)
        processedData = self._processingResponse(commandID, response)
        if processedData is not None:
            self._rows.append(processedData[0])
            return processedData[0]
        return None

    @property
    def table(self):
        return self._table

    @property
    def rows(self):
        return self._rows


g_ordersBook = _ReferenceBook(DatabaseTables.ORDERS)
