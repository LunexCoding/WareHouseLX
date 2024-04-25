from customtkinter import (CTkButton, CTkEntry)

from .context import Context
from .mainWindow import MainWindowContext
from commands.center import g_commandCenter
from commands.status import COMMAND_STATUS
from .consts import Constants


class AuthorizationWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.button = CTkButton(master=window, command=self._login)
        self.entryLogin = CTkEntry(master=window, placeholder_text="Логин")
        self.entryPassword = CTkEntry(master=window, placeholder_text="Пароль", show="*")
        self.entryLogin.pack(padx=20, pady=20)
        self.entryPassword.pack(padx=20, pady=20)
        self.button.pack(padx=20, pady=20)

    def _login(self):
        window = self._window
        result = g_commandCenter.execute(Constants.AUTHORIZATION_COMMAND.format(self.entryLogin.get(), self.entryPassword.get()))
        if result["Status"] == COMMAND_STATUS.EXECUTED:
            self.clear()
            window.changeContext(MainWindowContext)
        else:
            print("no")
