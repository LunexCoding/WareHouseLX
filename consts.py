from commands.consts import Constants as CMDConstants


class Constants:
    COMMAND_NOT_FOUND_MSG = "Command <{}> not found!"
    RESPONSE_STRING = "{}.{}.{}".replace(".", CMDConstants.SERVICE_SYMBOL)
    LOG_USER_INFO_STRING = "\tUserID<{}>\tName<{}>\t"
