from strenum import StrEnum


class DatabaseTables(StrEnum):
    ROLES = "Роли"
    USERS = "Пользователи"
    ORDERS = "Заказы"
    ORDER_DETAILS = "Детали_заказа"
    MACHINES = "Машины"


class ColumnsForInsertion:
    _tableColumns = {
        DatabaseTables.ORDERS.value: ["Client", "Comment", "CreationDate"]
    }

    @staticmethod
    def getColumns(tableName):
        return ColumnsForInsertion._tableColumns.get(tableName, [])
