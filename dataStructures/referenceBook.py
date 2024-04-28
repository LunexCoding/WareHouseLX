from database.tables import DatabaseTables, ColumnsForInsertion
from database.queries import SqlQueries
from database.database import DatabaseConnectionFactory
from settingsConfig import g_settingsConfig



class _ReferenceBook:
    def __init__(self, table, databaseFactory):
        self._table = table
        self._columns = None
        self._columnsForInsertion = None
        self._rowList = []
        self._loadedRecordsCount = 0
        self._sampleLimit = g_settingsConfig.DatabaseSettings["sampleLimit"]
        self.databaseFactory = databaseFactory

    def init(self):
        self._columns = self._getTableColumns()
        self._columnsForInsertion = ColumnsForInsertion.getColumns(self._table)

    def _getTableColumns(self):
        with self.databaseFactory.createConnection() as db:
            columns = db.getData(SqlQueries.getTableColumns(self._table), all=True)
        return [column[1] for column in columns]

    def loadRows(self):
        rows = self._loadRowsFromDB()
        if rows:
            self._rowList.extend(rows)
            self._loadedRecordsCount += len(rows)
            return self._rowList
        return None

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
        if not self._checkNextRowExists():
            self._insertRowToDB(row)
            return self.lastRowID
        return None

    def _insertRowToDB(self, row):
        columns = []
        for column in row.keys():
            if column in self._columnsForInsertion:
                columns.append(column)
        with self.databaseFactory.createConnection() as db:
            db.execute(
                SqlQueries.insertIntoTable(self._table, columns),
                data=list(row.values())
            )

    def _checkNextRowExists(self):
        with self.databaseFactory.createConnection() as db:
            rowID = db.getData(
                SqlQueries.getLastIDFromTable(self._table)
            )
            if rowID is not None:
                nextRowID = db.getData(
                    SqlQueries.selectRowFromTableByID(self._table, rowID[0] + 1)
                )
                return False if nextRowID is None else True
            return False

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

        with self.databaseFactory.createConnection() as db:
            rows = db.getData(
                SqlQueries.selectFromTable(self._table, requestData, limit, offset),
                all=True
            )
        result = []
        for row in rows:
            result.append({self._columns[i]: row[i] for i in range(len(self._columns))})
        if len(result) == 1:
            return result[0]
        return result

    @property
    def table(self):
        return self._table

    @property
    def columns(self):
        return self._columns

    @property
    def columnsForInsertion(self):
        return self._columnsForInsertion

    @property
    def rows(self):
        return self._rowList

    @property
    def lastRowID(self):
        with self.databaseFactory.createConnection() as db:
            return db.getData(
                SqlQueries.getLastIDFromTable(self._table)
            )[0]


class ReferenceBookFactory:
    def __init__(self, databaseFactory):
        self.databaseFactory = databaseFactory

    def createReferenceBook(self, table):
        return _ReferenceBook(table, self.databaseFactory)


g_referenceBookFactory = ReferenceBookFactory(DatabaseConnectionFactory(g_settingsConfig.DatabaseSettings["fullPath"]))

g_usersBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.USERS)
g_userRoles = g_referenceBookFactory.createReferenceBook(DatabaseTables.ROLES)
g_incomingDocumentsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.INCOMING_DOCUMENTS)
g_incomingDocumentDetailsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.INCOMING_DOCUMENT_DETAILS)
g_warehouseBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.WAREHOUSE)
g_outgoingDocuments = g_referenceBookFactory.createReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS)
g_outgoingDocumentDetailsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS_DETAILS)
g_warehouseOutgoingDetailsBook = g_referenceBookFactory.createReferenceBook(DatabaseTables.WAREHOUSE_OUTGOING_DETAILS)

g_referenceBooks = [
    g_usersBook,
    g_userRoles,
    g_incomingDocumentsBook,
    g_incomingDocumentDetailsBook,
    g_warehouseBook,
    g_outgoingDocuments,
    g_outgoingDocumentDetailsBook,
    g_warehouseOutgoingDetailsBook
]
