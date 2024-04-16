import os
import sys
import threading

from commands.center import g_commandCenter
from connection import Socket
from tools.logger import logger
from consts import Constants


_log = logger.getLogger(__name__)


class Server:
    def __init__(self):
        self.socket = None
        self.running = True

    def start(self):
        initBooksCommand = g_commandCenter.searchCommand("init")
        if initBooksCommand is not None:
            initBooksCommand.execute()
            self.socket = Socket(g_commandCenter)
            self.socket.start()
        else:
            _log.error(Constants.COMMAND_NOT_FOUND_MSG.format("init"))

    def stop(self):
        self.socket.stop()
        self.running = False


def userInputThread(server):
    while True:
        user_input = sys.stdin.readline().strip()
        if user_input == "stop":
            server.stop()
            os._exit(0)


if __name__ == "__main__":
    server = Server()
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    input_thread = threading.Thread(target=userInputThread, args=(server,))
    input_thread.start()

    server_thread.join()
    input_thread.join()
