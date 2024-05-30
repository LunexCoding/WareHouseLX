from strenum import StrEnum


class DatabaseTables(StrEnum):
    ROLES = "Роли"
    USERS = "Пользователи"
    ORDERS = "Заказы"
    ORDER_DETAILS = "Детали_заказа"
    MACHINES = "Машины"


class ColumnsForInsertion:
    _tableColumns = {
        DatabaseTables.USERS.value: ["Login", "Password", "RoleID", "Fullname"],
        DatabaseTables.ORDERS.value: ["Client", "MachineID", "Comment", "CreationDate"],
        DatabaseTables.MACHINES.value: ["Name", "Power", "Speed", "Direction", "Parameter1", "Parameter2", "Stage"]
    }

    @staticmethod
    def getColumns(tableName):
        return ColumnsForInsertion._tableColumns.get(tableName, [])
