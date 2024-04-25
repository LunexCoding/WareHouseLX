from customtkinter import (
    CTkButton,
    CTkLabel,
    CTkFrame
)

from settingsConfig import g_settingsConfig
from .context import Context
from .incomingDocuments import IncomingDocumentsWindowContext
from .consts import Constants


class MainWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.userRoleFrame = CTkFrame(window)
        self.userRoleLabel = CTkLabel(self.userRoleFrame, text=g_settingsConfig.role, font=Constants.FONT)
        self.userRoleFrame.grid(row=0, column=0, padx=10, pady=10)
        self.userRoleLabel.pack(padx=10, pady=10)

        self.buttonFrame = CTkFrame(window)
        self.buttonParish = CTkButton(self.buttonFrame, text="Приход", font=Constants.FONT, command=self._onButtonParish)
        self.buttonFrame.grid(row=0, column=1, padx=10, pady=10)
        self.buttonParish.grid(row=0, column=1, padx=10, pady=10)

        self.exitFrame = CTkFrame(window)
        self.buttonExit = CTkButton(self.exitFrame, text="Выйти", font=Constants.FONT, command=self._onButtonExit)
        self.exitFrame.grid(row=0, column=2, padx=10, pady=10)
        self.buttonExit.pack(padx=10, pady=10)

    def _onButtonParish(self):
        window = self._window
        self.clear()
        window.changeContext(IncomingDocumentsWindowContext)

    def _onButtonExit(self):
        self._window.close()
