from database.tables import DatabaseTables
from database.queries import SqlQueries
from database.database import DatabaseConnectionFactory
from settingsConfig import g_settingsConfig


class _ReferenceBook:
    def __init__(self, table, databaseFactory):
        self._table = table
        self._columns = None
        self._rowList = []
        self._loadedRecordsCount = 0
        self._sampleLimit = g_settingsConfig.DatabaseSettings["sampleLimit"]
        self.databaseFactory = databaseFactory

    def init(self):
        self._columns = self._getTableColumns()

    def _getTableColumns(self):
        with self.databaseFactory.createConnection() as db:
            columns = db.getData(SqlQueries.getTableColumns(self._table), all=True)
        return [column[1] for column in columns]

    def loadRows(self):
        rows = self._loadRowsFromDB()
        if rows:
            self._rowList.extend(rows)
            self._loadedRecordsCount += len(rows)

    def _loadRowsFromDB(self):
        with self.databaseFactory.createConnection() as db:
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
        with self.databaseFactory.createConnection() as db:
            db.execute(
                SqlQueries.insertIntoTable(self._table, columns),
                data=list(row.values())
            )

    def editRow(self, rowID, data):
        self._updateRowIntoDB(rowID, data)

    def _updateRowIntoDB(self, rowID, data):
        idColumn = self._columns[0]
        with self.databaseFactory.createConnection() as db:
            db.execute(
                SqlQueries.updateTable(self._table, idColumn, rowID, **data),
                data=list(data.values())
            )

    def deleteRow(self, rowID):
        self._deleteRowFromDB(rowID)

    def _deleteRowFromDB(self, rowID):
        idColumn = self._columns[0]
        with self.databaseFactory.createConnection() as db:
            db.execute(
                SqlQueries.deleteFromTable(self._table, idColumn, rowID)
            )

    def searchRowByParams(self, filterData, limit=None, offset=None):
        requestData = {
            "condition": filterData,
            "tableColumns": self._columns
        }
        SqlQueries.selectFromTable(self._table, requestData)
        with self.databaseFactory.createConnection() as db:
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


class ReferenceBookFactory:
    def __init__(self, databaseFactory):
        self.databaseFactory = databaseFactory

    def createReferenceBook(self, table):
        return _ReferenceBook(table, self.databaseFactory)


g_referenceBookFactory = ReferenceBookFactory(DatabaseConnectionFactory(g_settingsConfig.DatabaseSettings["fullPath"]))

g_usersBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.USERS)
g_incomingDocumentsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.INCOMING_DOCUMENTS)
g_incomingDocumentDetailsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.INCOMING_DOCUMENT_DETAILS)
g_warehouseBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.WAREHOUSE)
g_outgoingDocuments = g_referenceBookFactory.createReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS)
g_outgoingDocumentDetailsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS_DETAILS)
g_warehouseOutgoingDetailsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.WAREHOUSE_OUTGOING_DETAILS)

g_referenceBooks = [
    g_usersBook,
    g_incomingDocumentsBook,
    g_incomingDocumentDetailsBook,
    g_warehouseBook,
    g_outgoingDocuments,
    g_outgoingDocumentDetailsBook,
    g_warehouseOutgoingDetailsBook
]
