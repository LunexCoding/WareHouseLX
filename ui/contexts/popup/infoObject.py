from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, BOTH

from ui.contexts.context import Context


class InfoObject(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        name = data.get("Name", "Popup Info Window")
        window.title(name)
        window.geometry(f"250x{60 * (len(data['item']) + 1)}")
        window.resizable(False, False)
        window.focus()

        frame = CTkFrame(window)
        frame.pack(fill=BOTH, expand=True)

        for column, value in data["item"].items():
            CTkLabel(frame, text=column).pack()
            CTkEntry(frame, placeholder_text=value).pack()
        CTkButton(frame, text="Button").pack(pady=25)

