from dataStructures.dataObjs.dataObj import DataObj
from ui.contexts.popup.consts import Constants as ContextsConstants
from ui.widgets.consts import WidgetConstants


class Order(DataObj):
    _FIELDS = {
        "ID": {
            "text": "Номер",
            "size": ContextsConstants.ENTRY_WIDTH
        },
        "Client": {
            "text": "Клиент",
            "size": ContextsConstants.ENTRY_WIDTH,
            "type": str,
            "widget": WidgetConstants.ENTRY
        },
        "ContractNumber": {
            "text": "№ документа",
            "size": ContextsConstants.ENTRY_WIDTH,
            "type": str,
            "widget": WidgetConstants.ENTRY
        },
        "MachineID": {
            "text": "№ двигателя",
            "size": 75,
            "type": int,
            "widget": WidgetConstants.ENTRY
        },
        "CreationDate": {
            "text": "Дата создания",
            "size": ContextsConstants.ENTRY_WIDTH
        },
        "Comment": {
            "text": "Комментарий",
            "size": ContextsConstants.ENTRY_WIDTH,
            "type": str,
            "widget": WidgetConstants.ENTRY
        },
        "Status": {
            "text": "Статус",
            "size": ContextsConstants.ENTRY_WIDTH
        }
    }
    _INPUT_FIELDS = ["Client", "MachineID", "Comment"]
    _EDIT_FIELDS = ["Client", "ContractNumber", "MachineID", "Comment"]
    _GENERATED_FIELDS = ["CreationDate"]
    _MAIN_INPUT_FIELDS = ["Client"]

    def __init__(self, id, client, contractNumber, machineID, creationDate,  comment=None, status=None):
        self._id = int(id)
        self._client = client
        self._contractNumber = int(contractNumber)
        self._machineID = int(machineID)
        self._status = status
        self._creationDate = creationDate
        self._comment = comment if comment is not None else ""

    @property
    def data(self):
        return {
            "ID": self._id,
            "Client": self._client,
            "ContractNumber": self._contractNumber,
            "MachineID": self._machineID,
            "CreationDate": self._creationDate,
            "Comment": self._comment,
            "Status": self._status,
        }
