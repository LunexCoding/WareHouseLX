from database.tables import DatabaseTables


class Constants:
    INIT_BOOKS_HELP_MSG = """Загрузка данных в справочники."""
    INIT_DATABASE_HELP_MSG = """Инициализация базы данных."""
    TABLE_FOR_AUTHORZATION = DatabaseTables.USERS
    TABLE_ROLES = DatabaseTables.ROLES
    USER_NOT_FOUND = """Проверьте свои данные."""
    AUTHORIZATION_COMMAND_FAILED = "Команда не была выполнена."
    CLIENT_IS_NOT_AUTHORIZED_MSG = "Not authorized."
    ACCESS_ERROR_MSG = "Access error."
    CLIENT_NOT_ACCEPTED_MDG = "Client not accepted."
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
