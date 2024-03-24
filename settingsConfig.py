from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfigDB = self.__loadSettingsDB()
        self.__role = None

    def __loadSettingsDB(self):
        __settings = {}
        __settings["DATABASE"] = dict(
            database=config("DB_NAME"),
            databaseDirectory=config("DB_DIRECTORY")
        )
        return __settings

    @property
    def DatabaseSettings(self):
        return self.__settingsConfigDB["DATABASE"]

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role


g_settingsConfig = _SettingsConfig()
