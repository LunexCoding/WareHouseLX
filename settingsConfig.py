from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfigDB = self.__loadSettingsDB()

    def __loadSettingsDB(self):
        __settings = {}
        __settings["SERVER"] = dict(
            host=config("SERVER_HOST"),
            port=config("SERVER_PORT", cast=int)
        )
        __settings["LOG"] = dict(
            file=config("LOG_FILE"),
            directory=config("LOG_DIRECTORY")
        )
        return __settings

    @property
    def ServerSettings(self):
        return self.__settingsConfigDB["SERVER"]

    @property
    def LogSettings(self):
        return self.__settingsConfigDB["LOG"]


g_settingsConfig = _SettingsConfig()
