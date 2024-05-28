from customtkinter import END, CTkButton, CTkFrame, Y

from dataStructures.referenceBook import g_ordersBook
from dataStructures.order import Order
from ui.widgets import CommandButtonsWidget, PageNameWidget, TableWidget, UserInfoWidget
from user import g_user

from .consts import Constants
from .context import Context
from .popup.inputIOrder import InputOrderContext


class OrdersWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self._referenceBook = g_ordersBook

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user)
        PageNameWidget(self.frame, Constants.PAGE_ORDERS)
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

        self.table = TableWidget(window, Order).init()

        self.buttonLoad = CTkButton(window, text=Constants.BUTTON_LOAD_MORE, font=Constants.FONT, command=self._onButtonLoadClicked)
        self.buttonLoad.pack(padx=20, pady=20)
        self._loadRows()

    def _onButtonCreateClicked(self):
        self._window.openTopLevel(
            InputOrderContext,
            {
                "name": Constants.POPUP_WINDOW_NAME_INPUT_INCOMING_DOCUMENT,
                "command": self._save,
                "obj": Order
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

    def _onButtonLoadClicked(self):
        rows = self._referenceBook.loadRows()
        if rows is not None:
            self.displayRows(rows)

    def _save(self, row):
        self._window.topLevelWindow.close()
        result = self._referenceBook.insertRow(row)
        if result is not None:
            self.displayRows([result])

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
                self.table.insert("", END, values=list(row.data.values()))
