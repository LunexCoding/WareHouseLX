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
    createTableOrders = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.ORDERS} (
            `ID` INTEGER PRIMARY KEY,
            `Client` TEXT,
            `ContractNumber` INTEGER,
            `MachineID` INTEGER,
            `CreationDate` TEXT,
            `Comment` TEXT,
            `Status` TEXT DEFAULT 'В обработке',
            CONSTRAINT `chk_status` CHECK (Status IN ("В обработке", "В работе", "Завершен")),
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
            `Stage` TEXT
        );
    """
    # TRIGERS #
    createTriggerIncrementContractNumber = f"""
        CREATE TRIGGER IF NOT EXISTS IncrementContractNumber
        AFTER INSERT ON {DatabaseTables.ORDERS}
        BEGIN
            UPDATE {DatabaseTables.ORDERS}
            SET ContractNumber = (SELECT IFNULL(MAX(ContractNumber), 0) + 1 FROM {DatabaseTables.ORDERS} WHERE Client = NEW.Client)
            WHERE ID = NEW.ID;
        END;
    """
    createTriggerUpdateOrderStatus = f"""
        CREATE TRIGGER IF NOT EXISTS UpdateOrderStatusOnMachineStatusChange
        AFTER UPDATE OF Stage ON {DatabaseTables.MACHINES}
        FOR EACH ROW
        BEGIN
            UPDATE {DatabaseTables.ORDERS}
            SET Status = 
                CASE 
                    WHEN NEW.Stage = "Получение"
                        THEN "В обработке"
                    WHEN NEW.Stage != "Склад"
                        THEN "В работе"
                    ELSE "Завершен"
                END
            WHERE MachineID = NEW.ID;
        END;
        """
