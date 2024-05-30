from customtkinter import END, CTkButton, CTkFrame, Y

from dataStructures.referenceBook import g_usersBook
from dataStructures.dataObjs.user import User
from ui.widgets import CommandButtonsWidget, PageNameWidget, TableWidget, UserInfoWidget
from user import g_user

from .consts import Constants
from .context import Context
from ui.contexts.popup.user.inputContext import InputUserContext


class UsersContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self._referenceBook = g_usersBook

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user)
        PageNameWidget(self.frame, Constants.PAGE_USERS)
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

        self.table = TableWidget(window, User, self._editRow)

        self.buttonLoad = CTkButton(window, text=Constants.BUTTON_LOAD_MORE, font=Constants.FONT, command=self._onButtonLoadClicked)
        self.buttonLoad.pack(padx=20, pady=20)
        self._loadRows()

    def _onButtonCreateClicked(self):
        self._window.openTopLevel(
            InputUserContext,
            {
                "name": Constants.POPUP_WINDOW_NAME_INPUT_ORDER,
                "command": self._saveRow
            }
        )

    def _onButtonSearchClicked(self):
        ...

    def _onButtonRemoveClicked(self):
        selectedItem = self.table.selectedItem
        if selectedItem:
            rowID = selectedItem["values"][0]
            if self._referenceBook.removeRow(rowID) is not None:
                self.table.deleteRow(self.table.tree.selection()[0])

    def _onButtonBackClicked(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def _onButtonLoadClicked(self):
        rows = self._referenceBook.loadRows()
        if rows is not None:
            self.displayRows(rows)

    def _saveRow(self, row):
        self._window.topLevelWindow.close()
        result = self._referenceBook.addRow(row)
        if result is not None:
            self.displayRows([result])

    def _editRow(self, row):
        self._window.topLevelWindow.close()
        newRow = self._referenceBook.updateRow(row)
        self.table.updateRow(newRow)

    def _loadRows(self):
        if not self._referenceBook.rows:
            while True:
                rows = self._referenceBook.loadRows()
                if rows is None:
                    break
                self.displayRows(rows)
        else:
            self.displayRows(self._referenceBook.rows)

    def displayRows(self, rows):
        if rows is not None:
            for row in rows:
                self.table.insertRow("", END, values=list(row.data.values()))
