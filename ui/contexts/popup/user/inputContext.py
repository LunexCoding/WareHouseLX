from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, BOTH

from tools.fieldsGenerator import g_fieldsGenerator
from ui.contexts.context import Context
from ui.contexts.consts import Constants as ContextsConstants
from ui.widgets.errorLabel import ErrorLabel
from ui.contexts.popup.consts import Constants
from dataStructures.dataObjs.user import User


class InputUserContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._name = data.get("Name", Constants.DEFAULT_INPUT_WINDOW_NAME)
        self._command = data.get("command")
        self._entries = {}
        window.title(self._name)
        window.geometry(f"{Constants.WINDOW_WIDTH}x{Constants.DEFAULT_FIELD_HEIGHT * (len(User.getInputFields()) + 1)}")
        window.resizable(False, False)
        window.focus()

        self.frame = CTkFrame(window)
        self.errorLabel = ErrorLabel(
            self.frame,
            text_color=ContextsConstants.ERROR_LABEL_MSG_COLOR, font=Constants.FONT, wraplength=Constants.ERROR_LABEL_WRAP
        )
        # FIELDS
        # Login
        CTkLabel(
            self.frame,
            text=User.getInputFields()["Login"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        loginEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=User.getInputFields()["Login"]["size"]
        )
        loginEntry.pack(pady=5)
        # Password
        CTkLabel(
            self.frame,
            text=User.getInputFields()["Password"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        passwordEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=User.getInputFields()["Password"]["size"]
        )
        passwordEntry.pack(pady=5)
        # Role
        CTkLabel(
            self.frame,
            text=User.getInputFields()["Role"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        roleEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=User.getInputFields()["Role"]["size"]
        )
        roleEntry.pack(pady=5)
        # Fullname
        CTkLabel(
            self.frame,
            text=User.getInputFields()["Fullname"]["text"],
            font=Constants.FONT
        ).pack(pady=5)
        fullnameEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=User.getInputFields()["Fullname"]["size"]
        )
        fullnameEntry.pack(pady=5)

        self._entries["Login"] = loginEntry
        self._entries["Password"] = passwordEntry
        self._entries["Role"] = roleEntry
        self._entries["Fullname"] = fullnameEntry

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
        mainFieldsData = {column: entriesData[column] for column in User.getMainInputFields() if column in entriesData}
        namesMainFields = {field: fieldData["text"] for field, fieldData in User.getInputFields().items() if field in User.getMainInputFields()}
        if not all(len(value) != 0 for value in mainFieldsData.values()):
            missingMainFields = [column for column, value in mainFieldsData.items() if len(value) == 0]
            missingMainFieldsNames = ", ".join([namesMainFields[column] for column in missingMainFields])
            self.errorLabel.setText(Constants.ERROR_KEY_FIELDS_EMPTY_MSG.format(missingMainFieldsNames))
            return None

        for column, data in entriesData.items():
            if column in User.getInputFields():
                expectedType = User.getInputFields()[column].get("type")
                if expectedType:
                    try:
                        entriesData[column] = expectedType(data)
                    except ValueError:
                        self.errorLabel.setText(Constants.ERROR_TYPE_MSG.format(namesMainFields[column], expectedType.__name__))
                        return None

        if User.getGeneratedFields():
            fields = g_fieldsGenerator.generateFields(User.getGeneratedFields())
            if fields:
                for column, value in fields.items():
                    entriesData[column] = value

        return entriesData
