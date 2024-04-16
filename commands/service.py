from tools.logger import logger
from .command import BaseCommand
from .consts import Constants
from dataStructures.referenceBook import g_referenceBooks


_log = logger.getLogger(__name__)


class ServiceCommand(BaseCommand):
    def __init__(self):
        super().__init__()


class InitBooks(ServiceCommand):
    COMMAND_NAME = "init"

    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.INIT_BOOKS_HELP_MSG

    def execute(self, commandArgs=None):
        for book in g_referenceBooks:
            book.init()


commands = {
    InitBooks.COMMAND_NAME: InitBooks
}
