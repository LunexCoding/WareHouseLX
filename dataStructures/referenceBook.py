from commands.center import g_commandCenter
from commands.consts import Constants as CMDConstants, Commands
from commands.status import COMMAND_STATUS
from tools.dateConverter import convertTimestampToDate, isTimestamp
from tools.tables import DatabaseTables
from .order import Order


class _ReferenceBook:
    def __init__(self, table, dataObj):
        self._table = table
        self._rows = []
        self._dataObj = dataObj

    def _processingResponse(self, commandID, response):
        commandString = CMDConstants.SERVICE_SYMBOL.join([item.replace(CMDConstants.SERVICE_SYMBOL, " ") for item in response]).split()
        commandIDResponse = int(commandString.pop(0))
        commandStatus = int(commandString.pop(0))
        if commandID == commandIDResponse and commandStatus == COMMAND_STATUS.EXECUTED:
            rowString = ' '.join(commandString)
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
                rowData = [item.replace(CMDConstants.SERVICE_SYMBOL, " ") for item in rowData]
                rows[index] = self._dataObj(*rowData)
            return rows
        return None

    def loadRows(self):
        COMMAND_TYPE = CMDConstants.COMMAND_LOAD
        commandID = Commands.getCommandByType(COMMAND_TYPE, dict(table=self._table))
        response = g_commandCenter.execute(commandID)
        data = self._processingResponse(commandID, response)
        newData = []
        if data is not None:
            for dataObj in data:
                if not self._checkDataObj(dataObj.data["ID"]):
                    self._rows.append(dataObj)
                    newData.append(dataObj)
            return newData
        return None

    def insertRow(self, data):
        COMMAND_TYPE = CMDConstants.COMMAND_ADD
        commandID = Commands.getCommandByType(COMMAND_TYPE, dict(table=self._table))
        columns = "[*]"
        values = [",".join([value.replace(" ", CMDConstants.SERVICE_SYMBOL_FOR_ARGS) for value in map(str, data.values())])]
        command = CMDConstants.COMMAND_STRING.format(commandID, columns, values).replace("'", "")
        response = g_commandCenter.execute(command)
        dataObj = self._processingResponse(commandID, response)[0]
        if dataObj is not None:
            self._rows.append(dataObj)
            return dataObj
        return None

    def _checkDataObj(self, id):
        return id in [dataObj.data["ID"] for dataObj in self._rows]

    @property
    def table(self):
        return self._table

    @property
    def rows(self):
        return self._rows


g_ordersBook = _ReferenceBook(DatabaseTables.ORDERS, Order)
