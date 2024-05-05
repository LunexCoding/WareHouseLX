from datetime import datetime

from customtkinter import END, CTkButton, CTkFrame, Y

from dataStructures.referenceBook import g_bookIncomingDocuments
from ui.widgets import CommandButtonsWidget, PageNameWidget, TableWidget, UserInfoWidget
from user import g_user

from .consts import Constants
from .context import Context
from .popup.inputIncomingDocumentsWindow import InputIncomingDocumentsWindowContext


class IncomingDocumentsWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self._referenceBook = g_bookIncomingDocuments

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user)
        PageNameWidget(self.frame)
        CommandButtonsWidget(
            self.frame,
            commands={
                "create": self._onButtonCreateClicked,
                "search": self._onButtonSearchClicked,
                "remove": self._onButtonRemoveClicked,
                "back": self._onButtonBackClicked
            }
        )

        self.frame.pack(fill=Y, padx=10, pady=10)

        self.table = TableWidget(window, Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS).init()

        self.buttonLoad = CTkButton(window, text=Constants.BUTTON_LOAD_MORE, font=Constants.FONT, command=self._onButtonLoad)
        self.buttonLoad.pack(padx=20, pady=20)
        self._loadRows()

    def _onButtonCreateClicked(self):
        self._window.openTopLevel(
            InputIncomingDocumentsWindowContext,
            {
                "name": Constants.POPUP_WINDOW_NAME_INPUT_INCOMING_DOCUMENT,
                "command": self._saveDocument
            }
        )

    def _onButtonSearchClicked(self):
        ...

    def _onButtonRemoveClicked(self):
        ...

    def _onButtonBackClicked(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def _onButtonLoad(self):
        rows = self._referenceBook.loadRows()
        if rows is not None:
            self.displayRows(rows)

    def _saveDocument(self, row):
        self._window.topLevelWindow.close()
        result = self._referenceBook.insertRow(row)
        if result is not None:
            result["CreationDate"] = datetime.fromtimestamp(result["CreationDate"]).strftime(Constants.DATETIME_FORMAT)
            self.displayRows([result])

    def _loadRows(self):
        if not self._referenceBook.rows:
            rows = self._referenceBook.loadRows()
            self.displayRows(rows)
        else:
            self.displayRows(self._referenceBook.rows)

    def displayRows(self, rows):
        if rows is not None:
            for row in rows:
                values = [str(value) for value in row.values()]
                self.table.insert("", END, values=values)
