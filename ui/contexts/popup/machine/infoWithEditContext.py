from customtkinter import CTkFrame, CTkButton, CTkEntry, CTkLabel, BOTH

from tools.fieldsGenerator import g_fieldsGenerator
from ui.contexts.popup.consts import Constants
from ui.contexts.context import Context
from ui.contexts.consts import Constants as ContextsConstants
from ui.widgets.errorLabel import ErrorLabel


class InfoWithEditMachineContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", Constants.DEFAULT_INFO_WINDOW_NAME)
        self._command = data.get("command")
        self._dataObj = data["item"]
        self._entries = {}

        window.title(self._name)
        window.geometry(f"{Constants.WINDOW_WIDTH}x{Constants.DEFAULT_FIELD_HEIGHT * (len(self._dataObj.getFieldsForEditing()) + 2)}")
        window.focus()

        self.frame = CTkFrame(window)
        self.errorLabel = ErrorLabel(
            self.frame,
            text_color=ContextsConstants.ERROR_LABEL_MSG_COLOR, font=Constants.FONT,
            wraplength=Constants.ERROR_LABEL_WRAP
        )
        # FIELDS
        # Name
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Name"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        nameEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Name"]["size"]
        )
        nameEntry.insert(0, self._dataObj.data["Name"])
        nameEntry.pack(pady=5)
        # Power
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Power"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        powerEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Power"]["size"]
        )
        powerEntry.insert(0, self._dataObj.data["Power"])
        powerEntry.pack(pady=5)
        # Speed
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Speed"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        speedEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Speed"]["size"]
        )
        speedEntry.insert(0, self._dataObj.data["Speed"])
        speedEntry.pack(pady=5)
        # Direction
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Direction"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        directionEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Direction"]["size"]
        )
        directionEntry.insert(0, self._dataObj.data["Direction"])
        directionEntry.pack(pady=5)
        # Parameter1
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Parameter1"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        parameterFirstEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Parameter1"]["size"]
        )
        parameterFirstEntry.insert(0, self._dataObj.data["Parameter1"])
        parameterFirstEntry.pack(pady=5)
        # Parameter2
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Parameter2"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        parameterSecondEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Parameter2"]["size"]
        )
        parameterSecondEntry.insert(0, self._dataObj.data["Parameter2"])
        parameterSecondEntry.pack(pady=5)
        # Stage
        CTkLabel(
            self.frame,
            text=self._dataObj.getInputFields()["Stage"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        stageEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=self._dataObj.getInputFields()["Stage"]["size"]
        )
        stageEntry.insert(0, self._dataObj.data["Stage"])
        stageEntry.pack(pady=5)

        self._entries["Name"] = nameEntry
        self._entries["Power"] = powerEntry
        self._entries["Speed"] = speedEntry
        self._entries["Direction"] = directionEntry
        self._entries["Parameter1"] = parameterFirstEntry
        self._entries["Parameter2"] = parameterSecondEntry
        self._entries["Stage"] = stageEntry

        self.buttonSave = CTkButton(self.frame, text="Сохранить", command=self._onSaveButtonClicked)

        self.buttonSave.pack(pady=15)
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
