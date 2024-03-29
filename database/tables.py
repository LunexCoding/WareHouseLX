from strenum import StrEnum


class DatabaseTables(StrEnum):
    USERS = "Пользователи"
    ROLES = "Роли"
    INCOMING_DOCUMENTS = "Документы_прихода"
    INCOMING_DOCUMENT_DETAILS = "Детали_документа_прихода"
    WAREHOUSE = "Склад"
    OUTGOING_DOCUMENTS = "Документы_расхода"
    OUTGOING_DOCUMENTS_DETAILS = "Детали_документа_расхода"
    WAREHOUSE_OUTGOING_DETAILS = "Связь_Склад_и_Детали_документа_расхода"
