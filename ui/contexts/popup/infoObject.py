from customtkinter import CTkButton, CTkEntry, CTkScrollableFrame, CTkLabel, BOTH

from .consts import Constants
from ui.contexts.context import Context
from ui.contexts.consts import Constants as ContextsConstants
from ui.widgets.errorLabel import ErrorLabal


class InfoObject(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", "Popup Info Window")
        self._command = data.get("command")
        self._dataObj = data["item"]
        self._entries = {}

        window.title(self._name)
        window.geometry(f"{Constants.WINDOW_WIDTH}x{60 * (len(self._dataObj.getFieldsForEditing()) + 2)}")
        window.focus()

        self.frame = CTkScrollableFrame(window)
        self.errorLabel = ErrorLabal(
            self.frame, text=Constants.ERROR_KEY_FIELDS_EMPTY_MSG.format(", ".join(self._dataObj.getFieldsForEditing())),
            text_color=ContextsConstants.ERROR_LABEL_MSG_COLOR, font=Constants.FONT,
            wraplength=Constants.ERROR_LABEL_WRAP
        )
        for field in self._dataObj.getFieldsForEditing():
            CTkLabel(
                self.frame,
                text=self._dataObj.getFields()[field]["text"],
                font=Constants.FONT
            ).pack(pady=5)
            entry = CTkEntry(
                self.frame,
                font=Constants.FONT,
                width=self._dataObj.getFields()[field]["size"]
            )
            entry.insert(0, self._dataObj.data[field])
            entry.pack(pady=5)
            self._entries[field] = entry

        self.buttonSave = CTkButton(self.frame, text="Сохранить", command=self._onSaveButtonClicked)

        self.buttonSave.pack(pady=25)
        self.frame.pack(fill=BOTH, expand=True)

    def _onSaveButtonClicked(self):
        data = self._validate()
        if data is None:
            self.errorLabel.show()
        else:
            self.errorLabel.hide()
            self._command(data)

    def _validate(self):
        data = {column: None for column in self._dataObj.getFieldsForEditing().keys()}
        entriesData = {column: entry.get() for (column, entry) in self._entries.items()}
        mainEntriesData = [entriesData[column] for column in self._dataObj.getMainInputFields() if column in entriesData]

        if not all(len(column) for column in mainEntriesData):
            return None

        for column, value in entriesData.items():
            data[column] = value

        return data
