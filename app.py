from ui.windows import MainWindow


class App:
    def __init__(self):
        self._window = None

    def run(self):
        self._window = MainWindow()
        self._window.mainloop()
