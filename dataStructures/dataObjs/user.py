from dataStructures.dataObjs.dataObj import DataObj
from ui.contexts.popup.consts import Constants as ContextsConstants


class User(DataObj):
    _FIELDS = {
        "ID": {"text": "Номер", "size": ContextsConstants.ENTRY_WIDTH},
        "Login": {"text": "Логин", "size": ContextsConstants.ENTRY_WIDTH},
        "Password": {"text": "Пароль", "size": ContextsConstants.ENTRY_WIDTH},
        "Role": {"text": "Роль", "size": ContextsConstants.ENTRY_WIDTH},
        "Fullname": {"text": "ФИО", "size": ContextsConstants.ENTRY_WIDTH}
    }
    _INPUT_FIELDS = {
        "Login": {"text": "Логин", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "Password": {"text": "Пароль", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "RoleID": {"text": "Роль", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "Fullname": {"text": "Имя", "size": ContextsConstants.ENTRY_WIDTH, "type": str}
    }
    _GENERATED_FIELDS = ["CreationDate"]
    _MAIN_INPUT_FIELDS = ["Client"]

    def __init__(self, id, login, password, roleID, fullname):
        self._id = id
        self._login = login
        self._password = password
        self._roleID = roleID
        self._fullname = fullname

    @property
    def data(self):
        return {
            "ID": self._id,
            "Login": self._login,
            "Password": self._password,
            "RoleID": self._roleID,
            "Fullname": self._fullname
        }
