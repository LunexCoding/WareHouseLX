from datetime import datetime
from customtkinter import CTkLabel, CTkEntry, CTkFrame, CTkButton

from .consts import Constants
from ui.contexts.context import Context


class InputIncomingDocumentsWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        name = data.get("Name", "Popup Window")
        window.title(name)
        window.geometry("200x500")
        window.focus()

        self.frame = CTkFrame(window)
        CTkLabel(
            self.frame,
            text=Constants.INPUT_INCOMING_DOCUMENTS_FIELDS["Counterparty"]["text"],
            font=Constants.FONT
        ).pack(padx=10, pady=10)
        self.counterpartyEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=Constants.INPUT_INCOMING_DOCUMENTS_FIELDS["Counterparty"]["size"]
        )
        self.counterpartyEntry.pack(padx=10, pady=10)

        CTkLabel(
            self.frame,
            text=Constants.INPUT_INCOMING_DOCUMENTS_FIELDS["Comment"]["text"],
            font=Constants.FONT
        ).pack(padx=10, pady=10)
        self.commentEntry = CTkEntry(
            self.frame,
            font=Constants.FONT,
            width=Constants.INPUT_INCOMING_DOCUMENTS_FIELDS["Comment"]["size"]
        )
        self.commentEntry.pack(padx=10, pady=10)

        button_save = CTkButton(self.frame, text="Сохранить", command=lambda: data["command"](self._getFieldsData()))
        button_save.pack(side="right", padx=10, pady=10)
        self.frame.pack(pady=10, padx=10)

    def _getFieldsData(self):
        data = {column: None for column in Constants.INPUT_INCOMING_DOCUMENTS_FIELDS.keys()}
        counterparty = self.counterpartyEntry.get()
        comment = self.commentEntry.get()
        if all(len(column) for column in [counterparty]):
            data["Counterparty"] = counterparty
            data["CreationDate"] = datetime.timestamp(datetime.now())
            data["Comment"] = comment
            return data
        return None
