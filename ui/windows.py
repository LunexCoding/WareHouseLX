from customtkinter import CTk

from ui.contexts.authorizationWindow import AuthorizationWindowContext


class BaseWindow(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = None
        self.previousContext = None

    def close(self):
        CTk.destroy(self)

    def changeContext(self, contextClass, data=None):
        if contextClass is not None:
            self.previousContext = self.context.__class__
            self.context = contextClass(self, data)

    def returnToPrevious(self, data=None):
        self.changeContext(self.previousContext, data)


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.context = AuthorizationWindowContext(self, None)


