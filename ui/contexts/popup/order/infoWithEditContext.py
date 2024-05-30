from customtkinter import CTkFrame, CTkButton, CTkEntry, CTkLabel, BOTH

from tools.fieldsGenerator import g_fieldsGenerator
from ui.contexts.popup.consts import Constants
from ui.contexts.context import Context
from ui.contexts.consts import Constants as ContextsConstants
from ui.widgets.errorLabel import ErrorLabel


class InfoWithEditOrderContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", Constants.DEFAULT_INFO_WINDOW_NAME)
        self._command = data.get("command")
        self._dataObj = data["item"]
        self._entries = {}

        window.title(self._name)
        window.geometry(f"{Constants.WINDOW_WIDTH}x{60 * (len(self._dataObj.getFieldsForEditing()) + 2)}")
        window.focus()

        self.frame = CTkFrame(window)
        self.errorLabel = ErrorLabel(
            self.frame,
            text_color=ContextsConstants.ERROR_LABEL_MSG_COLOR, font=Constants.FONT,
            wraplength=Constants.ERROR_LABEL_WRAP
        )
        # FIELDS
        # Client
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Client"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        clientEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Client"]["size"]
        )
        clientEntry.insert(0, self._dataObj.data["Client"])
        clientEntry.pack(pady=5)
        # Comment
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Comment"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        commentEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Comment"]["size"]
        )
        commentEntry.insert(0, self._dataObj.data["Comment"])
        commentEntry.pack(pady=5)

        self._entries["Client"] = clientEntry
        self._entries["Comment"] = commentEntry

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
        entriesData = {column: entry.get() for (column, entry) in self._entries.items()}
        entriesData["ID"] = self._dataObj.data["ID"]
        mainFieldsData = {column: entriesData[column] for column in self._dataObj.getMainInputFields() if column in entriesData}
        namesMainFields = {field: fieldData["text"] for field, fieldData in self._dataObj.getInputFields().items() if field in self._dataObj.getMainInputFields()}
        if not all(len(value) != 0 for value in mainFieldsData.values()):
            missingMainFields = [column for column, value in mainFieldsData.items() if len(value) == 0]
            missingMainFieldsNames = ", ".join([namesMainFields[column] for column in missingMainFields])
            self.errorLabel.setText(Constants.ERROR_KEY_FIELDS_EMPTY_MSG.format(missingMainFieldsNames))
            return None

        for column, data in entriesData.items():
            if column in self._dataObj.getInputFields():
                expectedType = self._dataObj.getInputFields()[column].get("type")
                if expectedType:
                    try:
                        entriesData[column] = expectedType(data)
                    except ValueError:
                        self.errorLabel.setText(Constants.ERROR_TYPE_MSG.format(namesMainFields[column], expectedType.__name__))
                        return None

        if self._dataObj.getGeneratedFields():
            fields = g_fieldsGenerator.generateFields(self._dataObj.getGeneratedFields())
            if fields:
                for column, value in fields.items():
                    entriesData[column] = value

        return entriesData
