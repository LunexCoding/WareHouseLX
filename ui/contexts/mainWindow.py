import asyncio
from tkinter.ttk import Treeview, Scrollbar

from customtkinter import CTkButton, CTkFrame
from .context import Context
from .popup.inputAddWindow import InputAddWindowContext
from .consts import Constants
from client import CommandClient


class MainWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.client = CommandClient("localhost", 9999)

        self.tableFrame = CTkFrame(window)
        self.buttonAdd = CTkButton(self.tableFrame, text="Сложение", font=Constants.FONT, command=self._onButtonAdd)
        self.buttonAdd.pack(padx=10, pady=10)
        self.buttonUpdateTree = CTkButton(window, text="Обновить", font=Constants.FONT, command=self._onButtonUpdateTree)
        self.tableFrame.pack(side="top", fill="both", expand=True, pady=10, padx=10)
        self.buttonUpdateTree.pack(padx=10, pady=10)
        self.createTable()

    def createTable(self):
        self.tree = Treeview(self.tableFrame, columns=list(Constants.MAIN_WINDOWS_TREE_OPTIONS.keys()))
        for header, option in Constants.MAIN_WINDOWS_TREE_OPTIONS.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"], anchor="center")
        self.tree.column("#0", width=0, stretch=False)

        self.treeScroll = Scrollbar(self.tableFrame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        self.treeScroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)

    def _onButtonAdd(self):
        self._window.openTopLevel(
            InputAddWindowContext,
            {
                "name": "Сложение чисел",
                "command": self.getDataFromInputPopup
            }
        )

    def getDataFromInputPopup(self, data):
        self._window.topLevelWindow.close()
        asyncio.run(self._sendDataToServer(data))

    async def _sendDataToServer(self, data):
        await self.client.connect()
        result = await self.client.sendAndReceive(f"add {data['First']} {data['Second']}")
        self.client.close()
        self._saveResultCommandAdd(data, result)

    def _saveResultCommandAdd(self, data, result):
        print("Получен результат от сервера:", result)
        data["Result"] = result
        self.tree.insert("", "end", values=list(data.values()))

    def _onButtonUpdateTree(self):
        ...

    def _onButtonExit(self):
        self._window.close()