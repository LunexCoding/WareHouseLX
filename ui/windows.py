from customtkinter import CTk

from ui.contexts.authorizationWindow import AuthorizationWindowContext


class Window(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def close(self):
        CTk.destroy(self)


class MainWindow(Window):
    def __init__(self):
        super().__init__()

        self.context = AuthorizationWindowContext(self, None)

    def changeContext(self, contextClass, data=None):
        self.context = contextClass(self, data)
