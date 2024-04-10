from database.database import databaseSession
from database.tables import DatabaseTables
from database.queries import SqlQueries
from settingsConfig import g_settingsConfig


class _ReferenceBook:
    def __init__(self, table):
        self._table = table
        self._columns = None
        self._rowList = []
        self._loadedRecordsCount = 0
        self._sampleLimit = g_settingsConfig.DatabaseSettings["sampleLimit"]

    def init(self):
        self._columns = self._getTableColumns()

    def _getTableColumns(self):
        with databaseSession as db:
            columns = db.getData(SqlQueries.getTableColumns(self._table), all=True)
        return [column[1] for column in columns]

    def loadRows(self):
        rows = self._loadRowsFromDB()
        if rows:
            self._rowList.extend(rows)
            self._loadedRecordsCount += len(rows)

    def _loadRowsFromDB(self):
        with databaseSession as db:
            rows = db.getData(
                SqlQueries.selectFromTable(self._table, requestData="*", limit=self._sampleLimit, offset=self._loadedRecordsCount),
                all=True
            )
        result = []
        for row in rows:
            result.append({self._columns[i]: row[i] for i in range(len(self._columns))})
        return result

    def addRow(self, row):
        self._insertRowToDB(row)

    def _insertRowToDB(self, row):
        columns = []
        for column in row.keys():
            if column in self._columns:
                columns.append(column)
        with databaseSession as db:
            db.execute(
                SqlQueries.insertIntoTable(self._table, columns),
                data=list(row.values())
            )

    def editRow(self, rowID, data):
        self._updateRowIntoDB(rowID, data)

    def _updateRowIntoDB(self, rowID, data):
        idColumn = self._columns[0]
        with databaseSession as db:
            db.execute(
                SqlQueries.updateTable(self._table, idColumn, rowID, **data),
                data=list(data.values())
            )

    def deleteRow(self, rowID):
        self._deleteRowFromDB(rowID)

    def _deleteRowFromDB(self, rowID):
        idColumn = self._columns[0]
        with databaseSession as db:
            db.execute(
                SqlQueries.deleteFromTable(self._table, idColumn, rowID)
            )

    def searchRowByParams(self, filterData, limit=None, offset=None):
        requestData = {
            "condition": filterData,
            "tableColumns": self._columns
        }
        SqlQueries.selectFromTable(self._table, requestData)
        with databaseSession as db:
            rows = db.getData(
                SqlQueries.selectFromTable(self._table, requestData, limit, offset),
                all=True
            )
        result = []
        for row in rows:
            result.append({self._columns[i]: row[i] for i in range(len(self._columns))})
        return result

    @property
    def table(self):
        return self._table

    @property
    def columns(self):
        return self._columns

    @property
    def rows(self):
        return self._rowList


g_usersBook = _ReferenceBook(DatabaseTables.USERS)
g_incomingDocumentsBook = _ReferenceBook(DatabaseTables.INCOMING_DOCUMENTS)
g_incomingDocumentDetailsBook = _ReferenceBook(DatabaseTables.INCOMING_DOCUMENT_DETAILS)
g_warehouseBook = _ReferenceBook(DatabaseTables.WAREHOUSE)
g_outgoingDocuments = _ReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS)
g_outgoingDocumentDetailsBook = _ReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS_DETAILS)
g_warehouseOutgoingDetailsBook = _ReferenceBook(DatabaseTables.WAREHOUSE_OUTGOING_DETAILS)

g_referenceBooks = [
    g_usersBook,
    g_incomingDocumentsBook,
    g_incomingDocumentDetailsBook,
    g_warehouseBook,
    g_outgoingDocuments,
    g_outgoingDocumentDetailsBook,
    g_warehouseOutgoingDetailsBook
]
