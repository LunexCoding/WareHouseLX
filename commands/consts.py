from collections import namedtuple

from tools.tables import DatabaseTables


class Constants:
    SERVICE_SYMBOL = "\0"
    SERVICE_SYMBOL_FOR_ARGS = "\u2063"
    COMMAND_AUTHORIZATION = "auth"
    COMMAND_SEARCH = "search"
    COMMAND_LOAD = "load"
    COMMAND_ADD = "add"
    COMMAND_LONG = "long"
    COMMAND_STRING = "{}.{}.{}".replace(".", SERVICE_SYMBOL)


COMMAND = namedtuple("Command", ["id", "type", "params"])


class Commands:
    COMMAND_AUTHORIZATION = COMMAND(0, Constants.COMMAND_AUTHORIZATION, None)

    COMMAND_LOAD_ROLES = COMMAND(1, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ROLES))
    COMMAND_LOAD_USERS = COMMAND(2, Constants.COMMAND_LOAD, dict(table=DatabaseTables.USERS))
    COMMAND_LOAD_CLIENTS = COMMAND(3, Constants.COMMAND_LOAD, dict(table=DatabaseTables.CLIENTS))
    COMMAND_LOAD_WORKSHOPS = COMMAND(4, Constants.COMMAND_LOAD, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_LOAD_STAGES = COMMAND(5, Constants.COMMAND_LOAD, dict(table=DatabaseTables.STAGES))
    COMMAND_LOAD_ORDERS = COMMAND(6, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ORDERS))
    COMMAND_LOAD_ORDER_DETAILS = COMMAND(7, Constants.COMMAND_LOAD, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_LOAD_MACHINES = COMMAND(8, Constants.COMMAND_LOAD, dict(table=DatabaseTables.MACHINES))

    COMMAND_SEARCH_ROLES = COMMAND(9, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ROLES))
    COMMAND_SEARCH_USERS = COMMAND(10, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.USERS))
    COMMAND_SEARCH_CLIENTS = COMMAND(11, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.CLIENTS))
    COMMAND_SEARCH_WORKSHOPS = COMMAND(12, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.WORKSHOPS))
    COMMAND_SEARCH_STAGES = COMMAND(13, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.STAGES))
    COMMAND_SEARCH_ORDERS = COMMAND(14, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ORDERS))
    COMMAND_SEARCH_ORDER_DETAILS = COMMAND(15, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_SEARCH_MACHINES = COMMAND(16, Constants.COMMAND_SEARCH, dict(table=DatabaseTables.MACHINES))

    COMMAND_ADD_ROLE = COMMAND(17, Constants.COMMAND_ADD, dict(table=DatabaseTables.ROLES))
    COMMAND_ADD_USER = COMMAND(18, Constants.COMMAND_ADD, dict(table=DatabaseTables.USERS))
    COMMAND_ADD_CLIENT = COMMAND(19, Constants.COMMAND_ADD, dict(table=DatabaseTables.CLIENTS))
    COMMAND_ADD_ORDER = COMMAND(20, Constants.COMMAND_ADD, dict(table=DatabaseTables.ORDERS))
    COMMAND_ADD_ORDER_DETAIL = COMMAND(21, Constants.COMMAND_ADD, dict(table=DatabaseTables.ORDER_DETAILS))
    COMMAND_ADD_MACHINE = COMMAND(22, Constants.COMMAND_ADD, dict(table=DatabaseTables.MACHINES))

    COMMAND_LONG = COMMAND(23, Constants.COMMAND_LONG, None)

    @classmethod
    def getCommandByType(cls, type, params):
        for command in cls.__dict__.values():
            if isinstance(command, COMMAND) and command.type == type and command.params == params:
                return command.id
        return None

    @classmethod
    def getCommandByID(cls, commandID):
        for command in cls.__dict__.values():
            if isinstance(command, COMMAND) and command.id == commandID:
                return command
        return None
