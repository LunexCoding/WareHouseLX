from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfigDB = self.__loadSettingsDB()
        self.__role = None

    def __loadSettingsDB(self):
        __settings = {}
        __settings["SERVER"] = dict(
            host=config("SERVER_HOST"),
            port=config("SERVER_PORT", cast=int)
        )
        __settings["DATABASE"] = dict(
            sampleLimit=config("DB_LIMIT", cast=int)
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
    def DatabaseSettings(self):
        return self.__settingsConfigDB["DATABASE"]

    @property
    def LogSettings(self):
        return self.__settingsConfigDB["LOG"]

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def sampleLimit(self):
        return self.DatabaseSettings["sampleLimit"]


g_settingsConfig = _SettingsConfig()
