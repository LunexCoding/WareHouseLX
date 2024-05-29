from tkinter.ttk import Scrollbar, Treeview

from customtkinter import BOTH, CENTER, LEFT, RIGHT, TOP, VERTICAL, CTkFrame, Y

from .markup import MARCUP, TYPES_UI_MARKUP
from .widget import BaseWidget
from ui.contexts.popup.infoObject import InfoObject


class TableWidget(BaseWidget):
    def __init__(self, master, dataObj, editCommand):
        super().__init__(master)
        self._window = master
        self._dataObj = dataObj
        self._editCommand = editCommand
        self._columns = self._dataObj.getFields()
        self._selectedItem = None
        self._count = 1

        self.tableFrame = CTkFrame(self._window)
        self.tree = Treeview(self.tableFrame, columns=list(self._columns.keys()))
        for header, option in self._columns.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"], anchor=CENTER)
        self.tree.column("#0", width=0, stretch=False)
        self.treeScroll = Scrollbar(self.tableFrame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self._uiElements.append(MARCUP(element=self.tableFrame, type=TYPES_UI_MARKUP.PACK, side=TOP, fill=BOTH, expand=True, pady=10, padx=10))
        self._uiElements.append(MARCUP(element=self.treeScroll, type=TYPES_UI_MARKUP.PACK, side=RIGHT, fill=Y))
        self._uiElements.append(MARCUP(element=self.tree, type=TYPES_UI_MARKUP.PACK, side=LEFT, fill=BOTH, expand=True))
        self.tree.bind("<Double-1>", self._onDoubleClicked)
        self.tree.bind("<<TreeviewSelect>>", self._onSelectClicked)
        self.show()

    def insertRow(self, *args, **kwargs):
        self.tree.insert(iid=str(self._count), *args, **kwargs)
        self._count += 1

    def updateRow(self, dataObj):
        self.tree.item(str(dataObj.data["ID"]), values=list(dataObj.data.values()))

    def deleteRow(self, *items):
        self.tree.delete(*items)
        self._selectedItem = None

    def _onDoubleClicked(self, event):
        item = self.tree.selection()
        if item:
            itemObj = self._dataObj(*self.tree.item(item, "values"))
            self._createInfoPopupWindow(itemObj)

    def _onSelectClicked(self, event):
        selectedItem = self.tree.selection()
        if selectedItem:
            self._selectedItem = self.tree.item(selectedItem[0])

    def _createInfoPopupWindow(self, item):
        self._window.openTopLevel(
            InfoObject,
            {
                "name": "Popup Info",
                "item": item,
                "command": self._editCommand
            }
        )

    @property
    def selectedItem(self):
        return self._selectedItem
