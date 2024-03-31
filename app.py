from initializer.initializer import Initializer
from ui.windows import MainWindow

from dataStructures.referenceBook import g_usersBook


class App:
    def __init__(self):
        Initializer.run()

        self._window = None

    def run(self):
        # self._window = MainWindow()
        # self._window.mainloop()

        # g_usersBook.loadRows()
        # g_usersBook.loadRows()
        # g_usersBook.addRow({'Login': 'lx', 'lx': 'admin', 'RoleID': 1, 'Fullname': "lx"})
        # g_usersBook.editRow(6, {"Login": "nLogin", "Password": "nPassword"})
        # g_usersBook.deleteRow(6)
        g_usersBook.searchRowByParams()
