from customtkinter import (CTkButton, CTkEntry)

from .context import Context
from .mainWindow import MainWindowContext
from userAuthorization import Authorization



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
        if Authorization.login(self.entryLogin.get(), self.entryPassword.get()):
            self.clear()
            window.changeContext(MainWindowContext)
