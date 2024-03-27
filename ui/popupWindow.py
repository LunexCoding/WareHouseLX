from customtkinter import CTkToplevel


class PopupWindow(CTkToplevel):
    def __init__(self, contextClass, data=None):
        super().__init__()

        self.context = contextClass(self, data)
