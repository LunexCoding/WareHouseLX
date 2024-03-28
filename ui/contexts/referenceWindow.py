from customtkinter import CTkLabel, CTkButton

from .context import Context


class ReferenceWindow(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        name = data["name"]
        window.title(name)
        window.geometry("400x200")
        window.focus()
        CTkLabel(window, text=f"Информация о справочнике: {name}").pack(pady=20)
        buttonExit = CTkButton(window, text="Закрыть", command=window.destroy)
        buttonExit.pack()
