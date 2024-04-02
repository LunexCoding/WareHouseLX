import copy


class Constants:
    STORAGE_WINDOW_TREE_OPTIONS = {
        "Number": {"text": "Номер", "size": 100},
        "Conter": {"text": "Контрагент", "size": 100},
        "NumberTel": {"text": "Номер телефона", "size": 100},
        "Name": {"text": "Наименование груза", "size": 150},
        "Description": {"text": "Описание груза", "size": 150},
        "Type": {"text": "Тип тары", "size": 100},
        "Quantity": {"text": "Количество единиц", "size": 100},
        "Price": {"text": "Цена", "size": 100},
        "Creation Date": {"text": "Дата Создания", "size": 150},
        "Modification Date": {"text": "Дата Изменения", "size": 150}
    }
    PARISH_AND_EXPENSE_WINDOWS_TREE_OPTIONS = {
        "Doc number": {"text": "№ документа", "size": 100},
        "Conter": {"text": "Контрагент", "size": 100},
        "Contract number": {"text": "№ договора", "size": 100},
        "Creation Date": {"text": "Дата создания", "size": 100},
        "Status": {"text": "Статус", "size": 100},
        "Comment": {"text": "Комментарий", "size": 150}
    }
    PARISH_DOCUMENT_WINDOW_TREE_OPTIONS = copy.deepcopy(STORAGE_WINDOW_TREE_OPTIONS)
    PARISH_DOCUMENT_WINDOW_TREE_OPTIONS.pop("Modification Date")
    EXPENSE_DOCUMENT_WINDOW_TREE_OPTIONS = copy.deepcopy(STORAGE_WINDOW_TREE_OPTIONS)
    EXPENSE_DOCUMENT_WINDOW_TREE_OPTIONS.update(numberHoursInStock={"text": "Количество часов на складе", "size": 150})