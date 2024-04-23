from commands.client import Authorization


class Constants:
    COMMAND_NOT_FOUND_MSG = "Command <{}> not found!"
    COMMAND_INIT = "init"
    COMMAND_INIT_DATABASE = "init_db"
    AUTHORIZATION_COMMAND = Authorization.COMMAND_NAME
    CLIENT_IS_NOT_AUTHORIZED_MSG = "Not authorized."
    ACCESS_ERROR_MSG = "Access error."
