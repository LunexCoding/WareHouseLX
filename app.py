from initializer.initializer import Initializer
from ui.windows import MainWindow
from dataStructures.referenceBook import g_incomingDocumentsBook


class App:
    def __init__(self):
        Initializer.run()

        self._window = None

        g_incomingDocumentsBook.init()

    def run(self):
        self._window = MainWindow()
        self._window.mainloop()


