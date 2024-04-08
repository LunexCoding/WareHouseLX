from customtkinter import CTkLabel, CTkEntry, CTkFrame, CTkButton

from .consts import Constants
from ui.contexts.context import Context


class InputAddWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.data = data

        name = self.data.get("Name", "Popup Window")
        window.title(name)
        window.geometry("200x300")
        window.focus()

        self.frame = CTkFrame(window)

        CTkLabel(
            self.frame,
            text=Constants.INPUT_MAIN_WINDOWS_TREE_FIELDS["First"]["text"],
            font=Constants.FONT
        ).pack(padx=10, pady=10)
        self.firstNumber = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=Constants.INPUT_MAIN_WINDOWS_TREE_FIELDS["First"]["size"]
        )
        self.firstNumber.pack(padx=10, pady=10)

        CTkLabel(
            self.frame,
            text=Constants.INPUT_MAIN_WINDOWS_TREE_FIELDS["Second"]["text"],
            font=Constants.FONT
        ).pack(padx=10, pady=10)
        self.secondNumber = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=Constants.INPUT_MAIN_WINDOWS_TREE_FIELDS["Second"]["size"]
        )
        self.secondNumber.pack(padx=10, pady=10)

        button_save = CTkButton(self.frame, text="Сохранить", command=self._onButtonSaveClicled)
        button_save.pack(side="right", padx=10, pady=10)
        self.frame.pack(pady=10, padx=10)

    def _onButtonSaveClicled(self):
        return self.data["command"](self._getFieldsData())

    def _getFieldsData(self):
        data = {column: None for column in Constants.INPUT_MAIN_WINDOWS_TREE_FIELDS.keys()}
        firstNumber = self.firstNumber.get()
        secondNumber = self.secondNumber.get()
        if all(len(column) for column in [firstNumber, secondNumber]):
            data["First"] = firstNumber
            data["Second"] = secondNumber
            return data
        return None
