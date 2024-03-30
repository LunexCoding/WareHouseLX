from database.database import databaseSession
from database.tables import DatabaseTables
from database.queries import SqlQueries
from settingsConfig import g_settingsConfig


class _ReferenceBook:
    def __init__(self, table):
        self._table = table
        self._columns = self._getTableColumns()
        self._rowList = []
        self._loadedRecordsCount = 0
        self._sampleLimit = g_settingsConfig.sampleLimit

    def _getTableColumns(self):
        with databaseSession as db:
            columns = db.getData(SqlQueries.getTableColumns(self._table), all=True)
        return [column[1] for column in columns]

    def loadRows(self):
        rows = self._loadRowsFromDB()
        if rows:
            self._rowList.extend(rows)
            self._loadedRecordsCount += len(rows)  # Обновляем количество загруженных записей

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

    def addRow(self):
        ...

    def _insertRowToDB(self):
        ...

    def editRow(self):
        ...

    def _updateRowIntoDB(self):
        ...

    def deleteRow(self):
        ...

    def _deleteRowFromDB(self):
        ...

    def _searchRowByParams(self):
        ...

    @property
    def rows(self):
        return self._rowList


g_usersBook = _ReferenceBook(DatabaseTables.USERS)
# g_incomingDocumentsBook = _ReferenceBook(DatabaseTables.INCOMING_DOCUMENTS)
# g_incomingDocumentDetailsBook = _ReferenceBook(DatabaseTables.INCOMING_DOCUMENT_DETAILS)
# g_warehouseBook = _ReferenceBook(DatabaseTables.WAREHOUSE)
# g_outgoingDocuments = _ReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS)
# g_outgoingDocumentDetailsBook = _ReferenceBook(DatabaseTables.OUTGOING_DOCUMENTS_DETAILS)
# g_warehouseOutgoingDetailsBook = _ReferenceBook(DatabaseTables.WAREHOUSE_OUTGOING_DETAILS)
