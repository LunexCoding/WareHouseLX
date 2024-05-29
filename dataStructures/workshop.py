from .dataObj import DataObj
from ui.contexts.popup.consts import Constants as ContextsConstants


class Workshop(DataObj):
    _FIELDS = {
        "ID": {"text": "Номер", "size": ContextsConstants.ENTRY_WIDTH},
        "Name": {"text": "Наименование", "size": ContextsConstants.ENTRY_WIDTH}
    }
    _INPUT_FIELDS = {
        "Name": {"text": "Наименование", "size": ContextsConstants.ENTRY_WIDTH}
    }
    _MAIN_INPUT_FIELDS = ["Name"]

    def __init__(self, id, name):
        self._id = int(id)
        self._name = name

    @property
    def data(self):
        return {
            "ID": self._id,
            "Name": self._name
        }
