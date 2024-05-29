from strenum import StrEnum


class DatabaseTables(StrEnum):
    ROLES = "Роли"
    USERS = "Пользователи"
    WORKSHOPS = "Отделения"
    STAGES = "Этапы"
    ORDERS = "Заказы"
    ORDER_DETAILS = "Детали_заказа"
    MACHINES = "Машины"


class ColumnsForInsertion:
    _tableColumns = {
        DatabaseTables.ORDERS.value: ["Client", "Comment", "CreationDate"],
        DatabaseTables.WORKSHOPS.value: ["Name"]
    }

    @staticmethod
    def getColumns(tableName):
        return ColumnsForInsertion._tableColumns.get(tableName, [])
