from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, BOTH

from tools.fieldsGenerator import g_fieldsGenerator
from ui.contexts.context import Context
from ui.contexts.consts import Constants as ContextsConstants
from ui.widgets.errorLabel import ErrorLabel
from ui.contexts.popup.consts import Constants
from dataStructures.workshop import Workshop


class InputWorkshopContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", "Popup Input Window")
        self._command = data.get("command")
        self._entries = {}
        self._namesMainFields = {field: fieldData["text"] for field, fieldData in Workshop.getInputFields().items() if field in Workshop.getMainInputFields()}
        window.title(self._name)
        window.geometry(f"{Constants.WINDOW_WIDTH}x{60 * (len(Workshop.getInputFields()) + 3)}")
        window.resizable(False, False)
        window.focus()

        self.frame = CTkFrame(window)
        self.errorLabel = ErrorLabel(
            self.frame,
            text_color=ContextsConstants.ERROR_LABEL_MSG_COLOR, font=Constants.FONT, wraplength=Constants.ERROR_LABEL_WRAP
        )
        for field in Workshop.getInputFields():
            CTkLabel(
                self.frame,
                text=Workshop.getInputFields()[field]["text"],
                font=Constants.FONT
            ).pack(pady=5)
            entry = CTkEntry(
                self.frame,
                font=Constants.FONT,
                width=Workshop.getInputFields()[field]["size"]
            )
            entry.pack(pady=5)
            self._entries[field] = entry

        self.buttonSave = CTkButton(self.frame, text="Сохранить", command=self._onButtonSaveClicked)

        self.buttonSave.pack(pady=15)
        self.frame.pack(fill=BOTH, expand=True)

    def _onButtonSaveClicked(self):
        data = self._validate()
        if data is None:
            self.errorLabel.show()
        else:
            self.errorLabel.hide()
            self._command(data)

    def _validate(self):
        entriesData = {column: entry.get() for (column, entry) in self._entries.items()}
        mainFieldsData = {column: entriesData[column] for column in Workshop.getMainInputFields() if column in entriesData}
        if not all(len(value) != 0 for value in mainFieldsData.values()):
            missingMainFields = [column for column, value in mainFieldsData.items() if len(value) == 0]
            missingMainFieldsNames = ", ".join([self._namesMainFields[column] for column in missingMainFields])
            self.errorLabel.setText(Constants.ERROR_KEY_FIELDS_EMPTY_MSG.format(missingMainFieldsNames))
            return None

        if Workshop.getGeneratedFields():
            fields = g_fieldsGenerator.generateFields(Workshop.getGeneratedFields())
            if fields:
                for column, value in fields.items():
                    entriesData[column] = value

        return entriesData
