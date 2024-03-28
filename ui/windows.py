from customtkinter import CTk, CTkToplevel

from ui.contexts.authorizationWindow import AuthorizationWindowContext


class BaseWindow(CTk):
    def __init__(self):
        super().__init__()
        self.context = None
        self.previousContext = None
        self.topLevelWindow = None

    def close(self):
        CTk.destroy(self)

    def changeContext(self, contextClass, data=None):
        if contextClass is not None:
            self.previousContext = self.context.__class__
            self.context = contextClass(self, data)

    def returnToPrevious(self, data=None):
        self.changeContext(self.previousContext, data)

    def openTopLevel(self, contextClass, data=None):
        if self.topLevelWindow is None or not self.checkTopLevelWindow():
            self.topLevelWindow = PopupWindow(contextClass, data)  # create window if its None or destroyed
        else:
            self.topLevelWindow.focus()  # if window exists focus it

    def checkTopLevelWindow(self):
        return self.topLevelWindow.winfo_exists()


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.context = AuthorizationWindowContext(self, None)


class PopupWindow(CTkToplevel):
    def __init__(self, contextClass, data=None):
        super().__init__()

        self.context = contextClass(self, data)

    def close(self):
        CTkToplevel.destroy(self)
