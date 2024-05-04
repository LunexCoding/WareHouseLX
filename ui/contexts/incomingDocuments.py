from datetime import datetime
from tkinter.ttk import Treeview, Scrollbar
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkButton,
    E,
    Y,
    TOP,
    BOTH,
    VERTICAL,
    CENTER,
    LEFT,
    RIGHT,
    END
)

from user import g_user
from .context import Context
from .popup.inputIncomingDocumentsWindow import InputIncomingDocumentsWindowContext
from .consts import Constants
from dataStructures.referenceBook import g_bookIncomingDocuments
from ui.widgets.user import UserInfoWidget
from ui.widgets.pageName import PageNameWidget


class IncomingDocumentsWindowContext(Context):
    # константы типов констекстов
    def __init__(self, window, data):
        super().__init__(window, data)
        self._referenceBook = g_bookIncomingDocuments

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user).show()
        pageNameWidget = PageNameWidget(self.frame)

        self.buttonFrame = CTkFrame(self.frame)
        self.buttonCreateDocument = CTkButton(self.buttonFrame, text=Constants.BUTTON_CREATE, font=Constants.FONT, command=self._onCreateDocument)
        self.buttonSearch = CTkButton(self.buttonFrame, text=Constants.BUTTON_SEARCH, font=Constants.FONT)
        self.buttonRemove = CTkButton(self.buttonFrame, text=Constants.BUTTON_DELETE, font=Constants.FONT)
        self.buttonCreateDocument.grid(row=0, column=0, padx=10, pady=10)
        self.buttonSearch.grid(row=0, column=1, padx=10, pady=10)
        self.buttonRemove.grid(row=0, column=2, padx=10, pady=10)
        self.buttonFrame.grid(row=0, column=2, pady=10, padx=10)

        self.exitFrame = CTkFrame(self.frame)
        self.buttonBack = CTkButton(self.exitFrame, text=Constants.BUTTON_BACK, font=Constants.FONT, command=self._onButtonBack)
        self.buttonBack.pack(padx=10, pady=10)
        self.exitFrame.grid(row=0, column=3, padx=10, pady=10, sticky=E)

        self.frame.pack(fill=Y, padx=10, pady=10)

        self.tree = None
        self.treeScroll = None
        self.tableFrame = CTkFrame(window)
        self.tableFrame.pack(side=TOP, fill=BOTH, expand=True, pady=10, padx=10)

        self.createTable()
        self.buttonLoad = CTkButton(window, text=Constants.BUTTON_LOAD_MORE, font=Constants.FONT, command=self._onButtonLoad)
        self.buttonLoad.pack(padx=20, pady=20)
        self._loadRows()

    def createTable(self):
        self.tree = Treeview(self.tableFrame, columns=list(Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS.keys()))
        for header, option in Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"], anchor=CENTER)
        self.tree.column("#0", width=0, stretch=False)

        self.treeScroll = Scrollbar(self.tableFrame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self.treeScroll.pack(side=RIGHT, fill=Y)
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)

    def _onButtonBack(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def _onButtonLoad(self):
        rows = self._referenceBook.loadRows()
        if rows is not None:
            self.displayRows(rows)

    def _onCreateDocument(self):
        self._window.openTopLevel(
            InputIncomingDocumentsWindowContext,
            {
                "name": Constants.POPUP_WINDOW_NAME_INPUT_INCOMING_DOCUMENT,
                "command": self._saveDocument
            }
        )

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
                self.tree.insert("", END, values=values)
