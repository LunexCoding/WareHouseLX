import os
import threading

from commands.center import g_commandCenter
from connection import Socket
from tools.logger import logger
from consts import Constants


_log = logger.getLogger(__name__)


class Server:
    def __init__(self):
        self.socket = None
        self.running = False

    def start(self):
        self.running = True
        initBooksCommand = g_commandCenter.searchCommand(Constants.COMMAND_INIT)
        if initBooksCommand is not None:
            initBooksCommand.execute()
        else:
            _log.error(Constants.COMMAND_NOT_FOUND_MSG.format(Constants.COMMAND_INIT))
        self.socket = Socket(g_commandCenter)
        self.socket.start()

    def stop(self):
        self.socket.stop()
        self.running = False


if __name__ == "__main__":
    server = Server()
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    while True:
        user_input = input("-> ")
        if user_input == "stop":
            server.stop()
            os._exit(0)
