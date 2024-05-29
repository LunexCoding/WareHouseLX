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

    COMMAND_LOAD_ROLES = COMMAND(1, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ROLES))
    COMMAND_LOAD_USERS = COMMAND(2, Constants.COMMAND_LOAD, dict(table=DatabaseTables.USERS))
    COMMAND_LOAD_WORKSHOPS = COMMAND(3, Constants.COMMAND_LOAD, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_LOAD_STAGES = COMMAND(4, Constants.COMMAND_LOAD, dict(table=DatabaseTables.STAGES))
    COMMAND_LOAD_ORDERS = COMMAND(5, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ORDERS))
    COMMAND_LOAD_ORDER_DETAILS = COMMAND(6, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_LOAD_MACHINES = COMMAND(7, Constants.COMMAND_LOAD, dict(table=DatabaseTables.MACHINES))

    COMMAND_SEARCH_ROLES = COMMAND(8, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ROLES))
    COMMAND_SEARCH_USERS = COMMAND(9, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.USERS))
    COMMAND_SEARCH_WORKSHOPS = COMMAND(10, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_SEARCH_STAGES = COMMAND(11, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.STAGES))
    COMMAND_SEARCH_ORDERS = COMMAND(12, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ORDERS))
    COMMAND_SEARCH_ORDER_DETAILS = COMMAND(13, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_SEARCH_MACHINES = COMMAND(14, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.MACHINES))

    COMMAND_ADD_ROLE = COMMAND(15, Constants.COMMAND_ADD, dict(table=DatabaseTables.ROLES))
    COMMAND_ADD_USER = COMMAND(16, Constants.COMMAND_ADD, dict(table=DatabaseTables.USERS))
    COMMAND_ADD_WORKSHOP = COMMAND(17, Constants.COMMAND_ADD, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_ADD_STAGE = COMMAND(18, Constants.COMMAND_ADD, dict(table=DatabaseTables.STAGES))
    COMMAND_ADD_ORDER = COMMAND(19, Constants.COMMAND_ADD, dict(table=DatabaseTables.ORDERS))
    COMMAND_ADD_ORDER_DETAIL = COMMAND(20, Constants.COMMAND_ADD, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_ADD_MACHINE = COMMAND(21, Constants.COMMAND_ADD, dict(table=DatabaseTables.MACHINES))

    COMMAND_DELETE_ROLE = COMMAND(22, Constants.COMMAND_DELETE, dict(table=DatabaseTables.ROLES))
    COMMAND_DELETE_USER = COMMAND(23, Constants.COMMAND_DELETE, dict(table=DatabaseTables.USERS))
    COMMAND_DELETE_WORKSHOP = COMMAND(24, Constants.COMMAND_DELETE, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_DELETE_STAGE = COMMAND(25, Constants.COMMAND_DELETE, dict(table=DatabaseTables.STAGES))
    COMMAND_DELETE_ORDER = COMMAND(26, Constants.COMMAND_DELETE, dict(table=DatabaseTables.ORDERS))
    COMMAND_DELETE_ORDER_DETAIL = COMMAND(27, Constants.COMMAND_DELETE, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_DELETE_MACHINE = COMMAND(28, Constants.COMMAND_DELETE, dict(table=DatabaseTables.MACHINES))

    COMMAND_UPDATE_ROLE = COMMAND(29, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.ROLES))
    COMMAND_UPDATE_USER = COMMAND(30, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.USERS))
    COMMAND_UPDATE_WORKSHOP = COMMAND(31, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_UPDATE_STAGE = COMMAND(32, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.STAGES))
    COMMAND_UPDATE_ORDER = COMMAND(33, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.ORDERS))
    COMMAND_UPDATE_ORDER_DETAIL = COMMAND(34, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_UPDATE_MACHINE = COMMAND(35, Constants.COMMAND_UPDATE, dict(table=DatabaseTables.MACHINES))

    @classmethod
    def getCommandByID(cls, commandID):
        for command in cls.__dict__.values():
            if isinstance(command, COMMAND) and command.id == commandID:
                return command
        return None
