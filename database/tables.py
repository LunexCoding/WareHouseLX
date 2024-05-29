from strenum import StrEnum


class DatabaseTables(StrEnum):
    ROLES = "Роли"
    USERS = "Пользователи"
    CLIENTS = "Клиенты"
    WORKSHOPS = "Отделения"
    STAGES = "Этапы"
    ORDERS = "Заказы"
    ORDER_DETAILS = "Детали_заказа"
    MACHINES = "Машины"


class ColumnsForInsertion:
    _tableColumns = {
        DatabaseTables.ORDERS.value: ["Client", "Comment", "CreationDate"],
    }

    @staticmethod
    def getColumns(table_name):
        return ColumnsForInsertion._tableColumns.get(table_name, [])
