from database.tables import DatabaseTables


class SqlQueries:
    applyingSettings = """PRAGMA foreign_keys = ON"""
    createTableRoles = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.ROLES} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255)
        );
    """
    createTableUsers = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.USERS} (
            `ID` INTEGER PRIMARY KEY,
            `Login` VARCHAR(255),
            `Password` VARCHAR(255),
            `RoleID` INTEGER,
            `Fullname` VARCHAR(255),
            FOREIGN KEY (RoleID) REFERENCES {DatabaseTables.ROLES} (ID) ON DELETE SET NULL
        );
    """
    createTableIncomingDocuments = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.INCOMING_DOCUMENTS} (
            ID INTEGER PRIMARY KEY,
            Counterparty VARCHAR(255),
            ContractNumber INTEGER,
            Phone VARCHAR(11),
            CreationDate DATE,
            Comment TEXT
        );
    """
    createTableIncomingDocumentDetails = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.INCOMING_DOCUMENT_DETAILS} (
            ID INTEGER PRIMARY KEY,
            DocumentNumber INTEGER,
            CargoName TEXT,
            CargoDescription TEXT,
            PackagingType TEXT,
            Quantity INTEGER,
            Price REAL,
            CreationDate DATE,
            FOREIGN KEY (DocumentNumber) REFERENCES {DatabaseTables.INCOMING_DOCUMENTS}(ID)
        );
    """
    createTableWarehouse = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.WAREHOUSE} (
            ID INTEGER PRIMARY KEY,
            DocumentID INTEGER,
            DateOfChange DATE
        );
    """
    createTableOutgoingDocuments = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.OUTGOING_DOCUMENTS} (
            ID INTEGER PRIMARY KEY,
            Counterparty VARCHAR(255),
            ContractNumber INTEGER,
            Phone VARCHAR(11),
            CreationDate DATE,
            Comment TEXT
        );
    """
    createTableOutgoingDocumentDetails = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.OUTGOING_DOCUMENTS_DETAILS} (
            ID INTEGER PRIMARY KEY,
            DocumentID INTEGER,
            DepartureDate DATE,
            HoursOnWarehouse INTEGER
        );

    """
    createTableWarehouseOutgoingDetails = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.WAREHOUSE_OUTGOING_DETAILS} (
            ID INTEGER PRIMARY KEY,
            WarehouseID INTEGER,
            OutgoingDetailsID INTEGER,
            FOREIGN KEY (WarehouseID) REFERENCES Warehouse(ID),
            FOREIGN KEY (OutgoingDetailsID) REFERENCES OutgoingDocumentDetails(ID)
        );
    """
    createTriggerSetUserRole = f"""
        CREATE TRIGGER IF NOT EXISTS update_role_to_default 
        AFTER UPDATE ON {DatabaseTables.USERS}
        WHEN OLD.RoleID = 1 AND NEW.RoleID IS NULL
        BEGIN
            UPDATE {DatabaseTables.USERS}
            SET RoleID = (SELECT ID FROM {DatabaseTables.ROLES} WHERE Name = 'User')
            WHERE ID = OLD.ID;
        END;
    """
