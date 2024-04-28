from datetime import datetime
from tkinter.ttk import Treeview, Scrollbar

import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton

from .context import Context
from .popup.inputIncomingDocumentsWindow import InputIncomingDocumentsWindowContext
from .consts import Constants
from settingsConfig import g_settingsConfig
from dataStructures.referenceBook import g_bookIncomingDocuments


class IncomingDocumentsWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self._referenceBook = g_bookIncomingDocuments

        self.buttonFrame = CTkFrame(window)
        self.userRoleFrame = CTkFrame(self.buttonFrame)
        self.userRoleLabel = CTkLabel(self.userRoleFrame, text=g_settingsConfig.role, font=Constants.FONT)

        self.userRoleLabel.pack(side="left", padx=10, pady=10)
        self.userRoleFrame.pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(self.buttonFrame, text="Склад", font=Constants.FONT).pack(side="left", padx=10, pady=10)
        self.buttonFrame.pack(side="top", fill="x", pady=10, padx=10)

        self.buttonCreateDocument = ctk.CTkButton(self.buttonFrame, text="Создать документ", font=Constants.FONT, command=self._onCreateDocument)
        self.buttonCreateDocument.pack(side="left", padx=10, pady=10)
        self.buttonSearch = ctk.CTkButton(self.buttonFrame, text="Найти", font=Constants.FONT)
        self.buttonSearch.pack(side="left", padx=10, pady=10)
        self.buttonRemove = ctk.CTkButton(self.buttonFrame, text="Удалить", font=Constants.FONT)
        self.buttonRemove.pack(side="left", padx=10, pady=10)
        self.buttonBack = CTkButton(self.buttonFrame, text="Назад", font=Constants.FONT, command=self._onButtonBack)
        self.buttonBack.pack(side="left", padx=10, pady=10)

        self.tree = None
        self.treeScroll = None
        self.tableFrame = ctk.CTkFrame(window)
        self.tableFrame.pack(side="top", fill="both", expand=True, pady=10, padx=10)
        self.createTable()
        self._loadRows()

    def _onButtonBack(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def _onCreateDocument(self):
        self._window.openTopLevel(
            InputIncomingDocumentsWindowContext,
            {
                "name": "Создание документа прихода",
                "command": self._saveDocument
            }
        )

    def _saveDocument(self, row):
        self._window.topLevelWindow.close()
        dataForInsert = row.copy()
        del dataForInsert["ID"]
        del dataForInsert["ContractNumber"]
        result = self._referenceBook.insertRow(dataForInsert)
        if result is not None:
            result["CreationDate"] = datetime.fromtimestamp(result["CreationDate"]).strftime(Constants.DATETIME_FORMAT)
            values = [str(value) for value in result.values()]
            self.tree.insert("", "end", values=values)

    def _loadRows(self):
        rows = self._referenceBook.loadRows()
        if rows is not None:
            for row in rows:
                values = [str(value) for value in row.values()]
                self.tree.insert("", "end", values=values)

    def createTable(self):
        self.tree = Treeview(self.tableFrame, columns=list(Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS.keys()))
        for header, option in Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"], anchor="center")
        self.tree.column("#0", width=0, stretch=False)

        self.treeScroll = Scrollbar(self.tableFrame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self.treeScroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
