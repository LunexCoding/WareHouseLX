from pathlib import Path

from database.queries import SqlQueries as coreQueries
from database.tables import DatabaseTables
from settingsConfig import g_settingsConfig
from database.pipeline import DatabasePipeline
from .queries import SqlQueries
from .consts import Constants
from tools.fileSystem import FileSystem


class Initializer:
    @staticmethod
    def initializeDatabase():
        databaseCreationPipeline = DatabasePipeline()
        databaseCreationPipeline.addOperation(SqlQueries.applyingSettings)
        databaseCreationPipeline.addOperation(SqlQueries.createTableRoles)
        databaseCreationPipeline.addOperation(SqlQueries.createTableUsers)
        databaseCreationPipeline.addOperation(SqlQueries.createTableIncomingDocuments)
        databaseCreationPipeline.addOperation(SqlQueries.createTableIncomingDocumentDetails)
        databaseCreationPipeline.addOperation(SqlQueries.createTableWarehouse)
        databaseCreationPipeline.addOperation(SqlQueries.createTableOutgoingDocuments)
        databaseCreationPipeline.addOperation(SqlQueries.createTableOutgoingDocumentDetails)
        databaseCreationPipeline.addOperation(SqlQueries.createTableWarehouseOutgoingDetails)
        databaseCreationPipeline.run()

    @staticmethod
    def initializeDatabaseData():
        record = DatabasePipeline()
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.ROLES, ["Name"]), ["Admin"])
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.ROLES, ["Name"]), ["User"])
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.USERS, ["Login", "Password", "RoleID"]), ["admin", "admin", 1])
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.USERS, ["Login", "Password", "RoleID"]), ["user", "user", 2])
        record.addOperation(SqlQueries.createTriggerSetUserRole)
        record.run()

    @staticmethod
    def run():
        if not FileSystem.exists(Constants.DATA_DIRECTORY):
            FileSystem.makeDir(Constants.DATA_DIRECTORY)
        if not FileSystem.exists(Path(Constants.DATA_DIRECTORY) / g_settingsConfig.DatabaseSettings["database"]):
            Initializer.initializeDatabase()
            Initializer.initializeDatabaseData()
