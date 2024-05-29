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
