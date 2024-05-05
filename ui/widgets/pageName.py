from customtkinter import CTkFrame, CTkLabel

from ui.contexts.consts import Constants

from .markup import MARCUP, TYPES_UI_MARKUP
from .widget import BaseWidget


class PageNameWidget(BaseWidget):
    def __init__(self, parent, pageName):
        super().__init__(parent)
        self.pageNameFrame = CTkFrame(parent)
        self.pageNameLabel = CTkLabel(self.pageNameFrame, text=pageName, font=Constants.FONT)
        self.pageNameLabel.pack(padx=10, pady=10)
        self.pageNameFrame.grid(row=0, column=1, padx=10, pady=10)
        self._uiElements.append(MARCUP(element=self.pageNameFrame, type=TYPES_UI_MARKUP.GRID, row=0, column=1, padx=10, pady=10))
        self._uiElements.append(MARCUP(element=self.pageNameLabel, type=TYPES_UI_MARKUP.PACK, padx=10, pady=10))
        self.show()
