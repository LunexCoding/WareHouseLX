from customtkinter import CTkFrame, CTkLabel

from .widget import BaseWidget
from ui.contexts.consts import Constants


class PageNameWidget(BaseWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.pageNameFrame = CTkFrame(parent)
        self.pageNameLabel = CTkLabel(self.pageNameFrame, text=Constants.PAGE_INCOMING_DOCUMENTS, font=Constants.FONT)
        self.pageNameLabel.pack(padx=10, pady=10)
        self.pageNameFrame.grid(row=0, column=1, padx=10, pady=10)
