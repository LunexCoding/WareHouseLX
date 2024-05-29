from strenum import StrEnum


class DatabaseTables(StrEnum):
    USERS = "Пользователи"
    ORDERS = "Заказы"
    ORDER_DETAILS = "Детали_заказа"
    MACHINES = "Машины"
