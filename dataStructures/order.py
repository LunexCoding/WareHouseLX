from .dataObj import DataObj


class Order(DataObj):
    _FIELDS = {
        "ID": {"text": "Номер", "size": 50},
        "Client": {"text": "Клиент", "size": 100},
        "ContractNumber": {"text": "№ документа", "size": 100},
        "CreationDate": {"text": "Дата создания", "size": 100},
        "Comment": {"text": "Комментарий", "size": 150}
    }
    _INPUT_FIELDS = {
        "Client": {"text": "Клиент", "size": 100},
        "Comment": {"text": "Комментарий", "size": 150},
    }
    _GENERATED_FIELDS = ["CreationDate"]
    _MAIN_INPUT_FIELDS = ["Client"]

    def __init__(self, id, client, contractNumber, creationDate, comment=None):
        self._id = id
        self._client = client
        self._contractNumber = contractNumber
        self._creationDate = creationDate
        self._comment = comment.replace("\0", " ") if comment is not None else ""

    @property
    def data(self):
        return {
            "ID": self._id,
            "Client": self._client,
            "ContractNumber": self._contractNumber,
            "CreationDate": self._creationDate,
            "Comment": self._comment
        }
