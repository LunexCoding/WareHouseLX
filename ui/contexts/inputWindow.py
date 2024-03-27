from customtkinter import CTkLabel, CTkEntry

from .context import Context


class InputWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        name = data["name"]
        window.title(name)
        window.geometry("400x200")
        CTkLabel(window, text="Наименование:").pack()
        self.priceEntry = CTkEntry(window)
        self.priceEntry.pack()
