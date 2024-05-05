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
            `Login` VARCHAR(255) UNIQUE,
            `Password` VARCHAR(255),
            `RoleID` INTEGER,
            `Fullname` VARCHAR(255),
            FOREIGN KEY (`RoleID`) REFERENCES {DatabaseTables.ROLES}(`ID`)
        );
    """
    createTableClients = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.CLIENTS} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `Email` VARCHAR(255),
            `Phone` VARCHAR(255)
        );
    """
    createTableWorkshops = f"""
            CREATE TABLE IF NOT EXISTS {DatabaseTables.WORKSHOPS} (
                `ID` INTEGER PRIMARY KEY,
                `Name` VARCHAR(255)
            );
        """
    createTableStages = f"""
            CREATE TABLE IF NOT EXISTS {DatabaseTables.STAGES} (
                `ID` INTEGER PRIMARY KEY,
                `Name` VARCHAR(255),
                `Description` TEXT,
                `WorkshopID` INTEGER,
                FOREIGN KEY (`WorkshopID`) REFERENCES {DatabaseTables.WORKSHOPS}(`ID`)
            );
        """
    createTableOrders = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.ORDERS} (
            `ID` INTEGER PRIMARY KEY,
            `ClientID` INTEGER,
            `ContractNumber` INTEGER,
            `CreationDate` TEXT,
            `Comment` TEXT,
            FOREIGN KEY (`ClientID`) REFERENCES {DatabaseTables.CLIENTS}(`ID`)
        );
    """
    createTableOrderDetails = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.ORDER_DETAILS} (
            `ID` INTEGER PRIMARY KEY,
            `OrderID` INTEGER,
            `MachineID` INTEGER,
            `Comment` TEXT,
            `Status` TEXT,
            FOREIGN KEY (`OrderID`) REFERENCES {DatabaseTables.ORDERS}(`ID`),
            FOREIGN KEY (`MachineID`) REFERENCES {DatabaseTables.MACHINES}(`ID`)
        );
    """
    createTableMachines = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.MACHINES} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `Power` INTEGER,
            `Speed` INTEGER,
            `Direction` VARCHAR(255),
            `Parameter1` VARCHAR(255),
            `Parameter2` VARCHAR(255),
            `StageID` INTEGER,
            FOREIGN KEY (`StageID`) REFERENCES {DatabaseTables.STAGES}(`ID`)
        );
    """
    # TRIGERS #
    createTriggerSetUserRole = f"""
        CREATE TRIGGER IF NOT EXISTS UpdateRoleToDefault
        AFTER UPDATE ON {DatabaseTables.USERS}
        WHEN OLD.RoleID = 1 AND NEW.RoleID IS NULL
        BEGIN
            UPDATE {DatabaseTables.USERS}
            SET RoleID = (SELECT ID FROM {DatabaseTables.ROLES} WHERE Name = 'User')
            WHERE ID = OLD.ID;
        END;
    """
    createTriggerIncrementContractNumber = f"""
        CREATE TRIGGER IF NOT EXISTS IncrementContractNumber
        AFTER INSERT ON {DatabaseTables.ORDERS}
        BEGIN
            UPDATE {DatabaseTables.ORDERS}
            SET ContractNumber = (SELECT IFNULL(MAX(ContractNumber), 0) + 1 FROM {DatabaseTables.ORDERS} WHERE ClientID = NEW.ClientID)
            WHERE ID = NEW.ID;
        END;
    """
