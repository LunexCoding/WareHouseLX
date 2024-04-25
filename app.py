import threading

from ui.windows import MainWindow
from connection import g_socket
from tools.logger import logger


_log = logger.getLogger(__name__)


class App:
    def __init__(self):
        self._window = None

    def _runUI(self):
        self._window = MainWindow()
        self._window.mainloop()

    @staticmethod
    def _startSocket():
        try:
            _log.debug("Initializing socket...")
            g_socket.init()
        except Exception as e:
            _log.debug("Socket initialization failed: %s", e)

    def run(self):
        try:
            _log.debug("Starting app...")
            socket_thread = threading.Thread(target=self._startSocket)
            socket_thread.start()
            self._runUI()
        except Exception as e:
            _log.debug(e)


if __name__ == "__main__":
    app = App()
    app.run()
