from collections import namedtuple

from database.tables import DatabaseTables


class Constants:
    SERVICE_SYMBOL = "\0"
    SERVICE_SYMBOL_FOR_ARGS = "&"
    SERVER_COMMAND_INIT_DATABASE = "init_db"
    SERVER_COMMAND_INIT_BOOKS = "init"
    COMMAND_AUTHORIZATION = "auth"
    COMMAND_SEARCH = "search"
    COMMAND_LOAD = "load"
    COMMAND_ADD = "add"
    COMMAND_DELETE = "del"
    COMMAND_UPDATE = "upd"
    INIT_BOOKS_HELP_MSG = """Загрузка данных в справочники."""
    INIT_DATABASE_HELP_MSG = """Инициализация базы данных."""
    TABLE_FOR_AUTHORZATION = DatabaseTables.USERS
    TABLE_ROLES = DatabaseTables.ROLES
    USER_NOT_FOUND = """Проверьте свои данные."""
    AUTHORIZATION_COMMAND_FAILED = "Команда не была выполнена."
    CLIENT_IS_NOT_AUTHORIZED_MSG = "Not authorized."
    ACCESS_ERROR_MSG = "Access error."
    CLIENT_NOT_ACCEPTED_MDG = "Client not accepted."
    CREATION_DATE_FIELD = "CreationDate"


COMMAND = namedtuple("Command", ["id", "name", "params"])


class Commands:
    SERVER_COMMAND_INIT_DATABASE = COMMAND(-1, Constants.SERVER_COMMAND_INIT_DATABASE, None)
    SERVER_COMMAND_INIT_BOOKS = COMMAND(-2, Constants.SERVER_COMMAND_INIT_BOOKS, None)

    COMMAND_AUTHORIZATION = COMMAND(0, Constants.COMMAND_AUTHORIZATION, None)

    COMMAND_LOAD_USERS = COMMAND(1, Constants.COMMAND_LOAD, dict(table=DatabaseTables.USERS))
    COMMAND_LOAD_ORDERS = COMMAND(2, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ORDERS))
    COMMAND_LOAD_ORDER_DETAILS = COMMAND(3, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_LOAD_MACHINES = COMMAND(4, Constants.COMMAND_LOAD, dict(table=DatabaseTables.MACHINES))

    COMMAND_SEARCH_USERS = COMMAND(5, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.USERS))
    COMMAND_SEARCH_ORDERS = COMMAND(6, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ORDERS))
    COMMAND_SEARCH_ORDER_DETAILS = COMMAND(7, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_SEARCH_MACHINES = COMMAND(8, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.MACHINES))

    COMMAND_ADD_USER = COMMAND(9, Constants.COMMAND_ADD, dict(table=DatabaseTables.USERS))
    COMMAND_ADD_ORDER = COMMAND(10, Constants.COMMAND_ADD, dict(table=DatabaseTables.ORDERS))
    COMMAND_ADD_ORDER_DETAIL = COMMAND(11, Constants.COMMAND_ADD, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_ADD_MACHINE = COMMAND(12, Constants.COMMAND_ADD, dict(table=DatabaseTables.MACHINES))

    COMMAND_DELETE_USER = COMMAND(13, Constants.COMMAND_DELETE, dict(table=DatabaseTables.USERS))
    COMMAND_DELETE_ORDER = COMMAND(14, Constants.COMMAND_DELETE, dict(table=DatabaseTables.ORDERS))
    COMMAND_DELETE_ORDER_DETAIL = COMMAND(15, Constants.COMMAND_DELETE, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_DELETE_MACHINE = COMMAND(16, Constants.COMMAND_DELETE, dict(table=DatabaseTables.MACHINES))

    COMMAND_UPDATE_USER = COMMAND(17, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.USERS))
    COMMAND_UPDATE_ORDER = COMMAND(18, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.ORDERS))
    COMMAND_UPDATE_ORDER_DETAIL = COMMAND(19, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_UPDATE_MACHINE = COMMAND(20, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.MACHINES))

    @classmethod
    def getCommandByID(cls, commandID):
        for command in cls.__dict__.values():
            if isinstance(command, COMMAND) and command.id == commandID:
                return command
        return None
