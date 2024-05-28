from tkinter.ttk import Scrollbar, Treeview

from customtkinter import BOTH, CENTER, LEFT, RIGHT, TOP, VERTICAL, CTkFrame, Y

from .markup import MARCUP, TYPES_UI_MARKUP
from .widget import BaseWidget
from ui.contexts.popup.infoObject import InfoObject


class TableWidget(BaseWidget):
    def __init__(self, parent, dataObj):
        super().__init__(parent)
        self._window = parent
        self._dataObj = dataObj
        self._columns = self._dataObj.getFields()

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
        self.tree.bind("<Double-1>", self._onDoubleClick)

    def init(self):
        self.show()
        return self.tree

    def _onDoubleClick(self, event):
        item = self.tree.selection()
        if item:
            data = dict(zip([value["text"] for value in self._columns.values()], self.tree.item(item, "values")))
            print(data)
            self._createInfoPopupWindow(data)

    def _createInfoPopupWindow(self, item):
        self._window.openTopLevel(
            InfoObject,
            {
                "name": "Popup Info",
                "item": item
            }
        )
