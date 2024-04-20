from database.tables import DatabaseTables


class Constants:
    INIT_BOOKS_HELP_MSG = """Загрузка данных в справочники."""
    TABLE_FOR_AUTHORZATION = DatabaseTables.USERS
    TABLE_ROLES = DatabaseTables.ROLES
    USER_NOT_FOUND = """Проверьте свои данные."""
    AUTHORIZATION_COMMAND_FAILED = "Команда не была выполнена."
