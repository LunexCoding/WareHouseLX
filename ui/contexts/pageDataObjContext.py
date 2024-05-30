from customtkinter import END, CTkButton, CTkFrame, Y

from ui.widgets import CommandButtonsWidget, PageNameWidget, TableWidget, UserInfoWidget
from user import g_user
from tools.tables import DatabaseTables
from dataStructures.referenceBook import g_ordersBook
from .consts import Constants
from .context import Context
from .popup.dataObjContext import DataObjContext
from .popup.consts import DataObjContextType


class PageDataObjContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self._referenceBook = data["book"]
        self._dataObj = self._referenceBook.dataObj
        window.title(self._referenceBook.table)

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user)
        PageNameWidget(self.frame, self._referenceBook.table)
        CommandButtonsWidget(
            self.frame,
            g_user,
            commands={
                "create": self._onButtonCreateClicked,
                "search": self._onButtonSearchClicked,
                "remove": self._onButtonRemoveClicked,
                "back": self._onButtonBackClicked
            }
        )

        self.frame.pack(fill=Y, padx=10, pady=10)

        self.table = TableWidget(window, self._dataObj, self._editRow)

        self.buttonLoad = CTkButton(window, text=Constants.BUTTON_LOAD_MORE, font=Constants.FONT, command=self._onButtonLoadClicked)
        self.buttonLoad.pack(padx=20, pady=20)
        self._loadRows()

    def _onButtonCreateClicked(self):
        self._window.openTopLevel(
            DataObjContext,
            {
                "name": Constants.POPUP_WINDOW_NAME_INPUT,
                "command": self._saveRow,
                "dataObj": self._dataObj,
                "contextType": DataObjContextType.INPUT
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
        if self._referenceBook.table == DatabaseTables.MACHINES:
            orderRows = [obj.data for obj in g_ordersBook.rows]
            if not orderRows:
                g_ordersBook.loadRows()
                orderRows = [obj for obj in g_ordersBook.rows if obj.data["MachineID"] == newRow.data["ID"]]
            requiredRow = orderRows[0]
            if isinstance(requiredRow, dict):
                newOrderRow = g_ordersBook.search(f"MachineID = {requiredRow['MachineID']}")
                g_ordersBook.rows[g_ordersBook.rows.index(g_ordersBook.findDataObjByID(requiredRow["ID"]))] = newOrderRow
            else:
                newOrderRow = g_ordersBook.search(f"MachineID = {requiredRow.data['MachineID']}")
                g_ordersBook.rows[g_ordersBook.rows.index(requiredRow)] = newOrderRow

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
