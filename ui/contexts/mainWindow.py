from customtkinter import (
    CTkButton,
    CTkLabel,
    CTkFrame,
    Y
)

from .context import Context
from .incomingDocuments import IncomingDocumentsWindowContext
from ui.widgets import UserInfoWidget, PageNameWidget
from .consts import Constants
from user import g_user


class MainWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user)
        PageNameWidget(self.frame)

        self.buttonFrame = CTkFrame(self.frame)
        self.buttonParish = CTkButton(self.buttonFrame, text=Constants.PAGE_INCOMING_DOCUMENTS, font=Constants.FONT, command=self._onButtonParish)
        self.buttonParish.grid(row=0, column=1, padx=10, pady=10)
        self.buttonFrame.grid(row=0, column=1, padx=10, pady=10)

        self.exitFrame = CTkFrame(self.frame)
        self.buttonExit = CTkButton(self.exitFrame, text=Constants.BUTTON_EXIT, font=Constants.FONT, command=self._onButtonExit)
        self.buttonExit.pack(padx=10, pady=10)
        self.exitFrame.grid(row=0, column=2, padx=10, pady=10)

        self.frame.pack(fill=Y, padx=10, pady=10)

    def _onButtonParish(self):
        window = self._window
        self.clear()
        window.changeContext(IncomingDocumentsWindowContext)

    def _onButtonExit(self):
        self._window.close()
