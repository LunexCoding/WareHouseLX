from .command import BaseCommand
from connection import Socket
from tools.logger import logger
from dataStructures.referenceBook import g_referenceBooks


_log = logger.getLogger(__name__)


class ServiceCommand(BaseCommand):
    def __init__(self):
        super().__init__()


class InitBooks(ServiceCommand):
    COMMAND_NAME = "init"

    def execute(self, commandArgs=None):
        for book in g_referenceBooks:
            book.init()


class StartSocket(ServiceCommand):
    COMMAND_NAME = "start"

    def execute(self, commandArgs=None):
        commandCenter = commandArgs
        socket = Socket(commandCenter)
        return socket


class StopSocket(ServiceCommand):
    COMMAND_NAME = "stop"

    def execute(self, commandArgs=None):
        socket = commandArgs
        socket.stop()
        return socket


commands = {
    InitBooks.COMMAND_NAME: InitBooks,
    StartSocket.COMMAND_NAME: StartSocket,
    StopSocket.COMMAND_NAME: StopSocket
}
