from customtkinter import (
    CTkButton,
    CTkLabel,
    CTkFrame
)

from settingsConfig import g_settingsConfig
from .context import Context
from .subContext import SubContext
from .storageWindow import StorageWindowContext


class MainWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.userRoleFrame = CTkFrame(window)
        self.userRoleLabel = CTkLabel(self.userRoleFrame, text=g_settingsConfig.role, font=("Helvetica", 30))
        self.userRoleFrame.grid(row=0, column=0, padx=10, pady=10)
        self.userRoleLabel.pack(padx=10, pady=10)

        self.buttonFrame = CTkFrame(window)
        self.buttonStorage = CTkButton(self.buttonFrame, text="Склад", font=("Helvetica", 30), command=self._onButtonStorage)
        self.buttonParish = CTkButton(self.buttonFrame, text="Приход", font=("Helvetica", 30), command=self._onButtonParish)
        self.buttonExpense = CTkButton(self.buttonFrame, text="Расход", font=("Helvetica", 30), command=self._onButtonExpense)
        self.buttonService = CTkButton(self.buttonFrame, text="Сервис", font=("Helvetica", 30), command=self._onButtonService)
        self.buttonFrame.grid(row=0, column=1, padx=10, pady=10)
        self.buttonStorage.grid(row=0, column=0, padx=10, pady=10)
        self.buttonParish.grid(row=0, column=1, padx=10, pady=10)
        self.buttonExpense.grid(row=0, column=2, padx=10, pady=10)
        self.buttonService.grid(row=0, column=3, padx=10, pady=10)

        self.exitFrame = CTkFrame(window)
        self.buttonExit = CTkButton(self.exitFrame, text="Выйти", font=("Helvetica", 30), command=self._onButtonExit)
        self.exitFrame.grid(row=0, column=2, padx=10, pady=10)
        self.buttonExit.pack(padx=10, pady=10)

    def _onButtonStorage(self):
        window = self._window
        self.clear()
        window.changeContext(SubContext, {"text": "Label text"})

    def _onButtonParish(self):
        window = self._window
        self.clear()
        window.changeContext(StorageWindowContext)

    def _onButtonExpense(self):
        ...

    def _onButtonService(self):
        ...

    def _onButtonExit(self):
        self._window.close()
