from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, BOTH, CTkScrollableFrame

from tools.fieldsGenerator import g_fieldsGenerator
from ui.contexts.context import Context
from ui.contexts.consts import Constants as ContextsConstants
from ui.widgets.errorLabel import ErrorLabal
from .consts import Constants


class InputOrderContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", "Popup Window")
        self._command = data.get("command")
        self._dataObj = data.get("obj")
        self._entries = {}
        window.title(self._name)
        window.geometry(f"{Constants.WINDOW_WIDTH}x{60 * (len(self._dataObj.getInputFields()) + 3)}")
        window.focus()

        self.frame = CTkScrollableFrame(window)
        namesMainFields = [field_data["text"] for field, field_data in self._dataObj.getInputFields().items() if field in self._dataObj.getMainInputFields()]
        self.errorLabel = ErrorLabal(
            self.frame, text=Constants.ERROR_KEY_FIELDS_EMPTY_MSG.format(", ".join(namesMainFields)),
            text_color=ContextsConstants.ERROR_LABEL_MSG_COLOR, font=Constants.FONT, wraplength=Constants.ERROR_LABEL_WRAP
        )
        for field in self._dataObj.getInputFields():
            CTkLabel(
                self.frame,
                text=self._dataObj.getInputFields()[field]["text"],
                font=Constants.FONT
            ).pack(pady=5)
            entry = CTkEntry(
                self.frame,
                font=Constants.FONT,
                width=self._dataObj.getInputFields()[field]["size"]
            )
            entry.pack(pady=5)
            self._entries[field] = entry

        self.buttonSave = CTkButton(self.frame, text="Сохранить", command=self._onButtonSaveClicked)

        self.buttonSave.pack(pady=25)
        self.frame.pack(fill=BOTH, expand=True)

    def _onButtonSaveClicked(self):
        data = self._validate()
        if data is None:
            self.errorLabel.show()
        else:
            self.errorLabel.hide()
            self._command(data)

    def _validate(self):
        data = {column: None for column in self._dataObj.getInputFields().keys()}
        entriesData = {column: entry.get() for (column, entry) in self._entries.items()}
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
