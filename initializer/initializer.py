from database.queries import SqlQueries as coreQueries
from database.tables import DatabaseTables
from database.pipeline import DatabasePipeline
from .queries import SqlQueries
from settingsConfig import g_settingsConfig
from tools.fileSystem import FileSystem
from tools.logger import logger


_log = logger.getLogger(__name__)


class Initializer:
    @staticmethod
    def initializeDatabase():
        _log.debug("Database creation...")
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
    def initializeDatabaseTriggers():
        _log.debug("Creating triggers...")
        triggersCreatePipeLine = DatabasePipeline()
        triggersCreatePipeLine.addOperation(SqlQueries.createTriggerSetUserRole)
        triggersCreatePipeLine.addOperation(SqlQueries.createTriggerIncrementDocumentNumber)
        triggersCreatePipeLine.addOperation(SqlQueries.createTriggerIncrementCargoID)
        triggersCreatePipeLine.run()

    @staticmethod
    def initializeDatabaseData():
        _log.debug("Data recording...")
        record = DatabasePipeline()
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.ROLES, ["Name"]), ["Admin"])
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.ROLES, ["Name"]), ["User"])
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.USERS, ["Login", "Password", "RoleID"]), ["admin", "admin", 1])
        record.addOperation(coreQueries.insertIntoTable(DatabaseTables.USERS, ["Login", "Password", "RoleID"]), ["user", "user", 2])
        record.run()

    @staticmethod
    def run():
        if not FileSystem.exists(g_settingsConfig.DatabaseSettings["databaseDirectory"]):
            FileSystem.makeDir(g_settingsConfig.DatabaseSettings["databaseDirectory"])
            if not FileSystem.exists(g_settingsConfig.DatabaseSettings["fullPath"]):
                _log.debug("Initializing the Database...")
                Initializer.initializeDatabase()
                Initializer.initializeDatabaseTriggers()
                Initializer.initializeDatabaseData()
                _log.debug("Database initialized.")
                return True
        _log.debug("The database already exists.")
        return False
