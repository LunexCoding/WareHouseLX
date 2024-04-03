from initializer.initializer import Initializer
from ui.windows import MainWindow


class App:
    def __init__(self):
        Initializer.run()

        self._window = None

    def run(self):

        self._window = MainWindow()
        self._window.mainloop()

        # g_incomingDocumentsBook.addRow(
        #     {
        #         "Counterparty": "Котн 1"
        #     }
        # )
        # g_incomingDocumentsBook.addRow(
        #     {
        #         "Counterparty": "Котн 1"
        #     }
        # )
        # g_incomingDocumentsBook.addRow(
        #     {
        #         "Counterparty": "Котн 2"
        #     }
        # )
