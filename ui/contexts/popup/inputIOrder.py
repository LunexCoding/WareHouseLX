from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, BOTH, CTkTextbox

from tools.fieldsGenerator import g_fieldsGenerator
from ui.contexts.context import Context
from .consts import Constants


class InputOrderContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", "Popup Window")
        self._dataObj = data.get("obj")
        self._entries = {}
        window.title(self._name)
        window.geometry(f"250x{60 * (len(self._dataObj.getInputFields()) + 2)}")
        # window.resizable(False, False)
        window.focus()

        self.frame = CTkFrame(window)
        self.frame.pack(fill=BOTH, expand=True)
        for field in self._dataObj.getInputFields():
            CTkLabel(
                self.frame,
                text=self._dataObj.getInputFields()[field]["text"],
                font=Constants.FONT
            ).pack(pady=5)
            entry = CTkTextbox(
                self.frame,
                font=Constants.FONT,
                wrap="word"
            )
            entry.pack(pady=5)
            self._entries[field] = entry

        buttonSave = CTkButton(self.frame, text="Сохранить", command=lambda: data["command"](self._getFieldsData()))
        buttonSave.pack(pady=25)

    def _getFieldsData(self):
        data = {column: None for column in self._dataObj.getInputFields().keys()}
        entriesData = {column: value.get("1.0", "end-1c") for (column, value) in self._entries.items()}
        mainEntriesData = [entriesData[column] for column in self._dataObj.getMainInputFields() if column in entriesData]

        if not all(len(column) for column in mainEntriesData):
            return None

        for column, value in entriesData.items():
            data[column] = value

        if self._dataObj.getGeneratedFields():
            fields = g_fieldsGenerator.generateFields(self._dataObj.getGeneratedFields())
            if fields:
                for column, value in fields.items():
                    data[column] = value
        return data
