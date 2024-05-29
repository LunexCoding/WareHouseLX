from .dataObj import DataObj
from ui.contexts.popup.consts import Constants as ContextsConstants


class Order(DataObj):
    _FIELDS = {
        "ID": {"text": "Номер", "size": ContextsConstants.ENTRY_WIDTH},
        "Client": {"text": "Клиент", "size": ContextsConstants.ENTRY_WIDTH},
        "ContractNumber": {"text": "№ документа", "size": ContextsConstants.ENTRY_WIDTH},
        "CreationDate": {"text": "Дата создания", "size": ContextsConstants.ENTRY_WIDTH},
        "Comment": {"text": "Комментарий", "size": ContextsConstants.ENTRY_WIDTH}
    }
    _INPUT_FIELDS = {
        "Client": {"text": "Клиент", "size": ContextsConstants.ENTRY_WIDTH},
        "Comment": {"text": "Комментарий", "size": ContextsConstants.ENTRY_WIDTH},
    }
    _GENERATED_FIELDS = ["CreationDate"]
    _MAIN_INPUT_FIELDS = ["Client"]

    def __init__(self, id, client, contractNumber, creationDate, comment=None):
        self._id = int(id)
        self._client = client
        self._contractNumber = int(contractNumber)
        self._creationDate = creationDate
        self._comment = comment if comment is not None else ""

    @property
    def data(self):
        return {
            "ID": self._id,
            "Client": self._client,
            "ContractNumber": self._contractNumber,
            "CreationDate": self._creationDate,
            "Comment": self._comment
        }
