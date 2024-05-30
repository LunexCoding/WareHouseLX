from dataStructures.dataObjs.dataObj import DataObj
from ui.contexts.popup.consts import Constants as ContextsConstants


class Machine(DataObj):
    _FIELDS = {
        "ID": {"text": "Номер", "size": 50},
        "Name": {"text": "Наименование", "size": ContextsConstants.ENTRY_WIDTH},
        "Power": {"text": "Мощность", "size": 75},
        "Speed": {"text": "Обороты", "size": 75},
        "Direction": {"text": "Направление", "size": ContextsConstants.ENTRY_WIDTH},
        "Parameter1": {"text": "Параметр 1", "size": ContextsConstants.ENTRY_WIDTH},
        "Parameter2": {"text": "Параметр 2", "size": ContextsConstants.ENTRY_WIDTH},
        "Stage": {"text": "Этап", "size": ContextsConstants.ENTRY_WIDTH},
    }
    _INPUT_FIELDS = {
        "Name": {"text": "Наименование", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "Power": {"text": "Мощность", "size": 75, "type": int},
        "Speed": {"text": "Обороты", "size": 75, "type": int},
        "Direction": {"text": "Направление", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "Parameter1": {"text": "Параметр 1", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "Parameter2": {"text": "Параметр 2", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
        "Stage": {"text": "Этап", "size": ContextsConstants.ENTRY_WIDTH, "type": str},
    }
    _MAIN_INPUT_FIELDS = ["Name", "Power", "Speed", "Direction", "Parameter1", "Parameter2", "Stage"]

    def __init__(self, id, name, power, speed, direction, parameterFirst, parameterSecond, stage):
        self._id = int(id)
        self._name = name
        self._power = int(power)
        self._speed = int(speed)
        self._direction = direction
        self._parameterFirst = parameterFirst
        self._parameterSecond = parameterSecond
        self._stage = stage

    @property
    def data(self):
        return {
            "ID": self._id,
            "Name": self._name,
            "Power": self._power,
            "Speed": self._speed,
            "Direction": self._direction,
            "Parameter1": self._parameterFirst,
            "Parameter2": self._parameterSecond,
            "Stage": self._stage
        }
