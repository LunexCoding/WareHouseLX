from tkinter.ttk import Scrollbar, Treeview

from customtkinter import BOTH, CENTER, LEFT, RIGHT, TOP, VERTICAL, CTkFrame, Y

from .markup import MARCUP, TYPES_UI_MARKUP
from .widget import BaseWidget


class TableWidget(BaseWidget):
    def __init__(self, parent, columns):
        super().__init__(parent)
        self.tableFrame = CTkFrame(parent)
        self.tree = Treeview(self.tableFrame, columns=list(columns.keys()))
        for header, option in columns.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"], anchor=CENTER)
        self.tree.column("#0", width=0, stretch=False)
        self.treeScroll = Scrollbar(self.tableFrame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self._uiElements.append(MARCUP(element=self.tableFrame, type=TYPES_UI_MARKUP.PACK, side=TOP, fill=BOTH, expand=True, pady=10, padx=10))
        self._uiElements.append(MARCUP(element=self.treeScroll, type=TYPES_UI_MARKUP.PACK, side=RIGHT, fill=Y))
        self._uiElements.append(MARCUP(element=self.tree, type=TYPES_UI_MARKUP.PACK, side=LEFT, fill=BOTH, expand=True))

    def init(self):
        self.show()
        return self.tree
