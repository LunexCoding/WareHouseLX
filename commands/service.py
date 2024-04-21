from tools.logger import logger
from .command import BaseCommand
from .consts import Constants
from dataStructures.referenceBook import g_referenceBooks
from initializer.initializer import Initializer


_log = logger.getLogger(__name__)


class ServiceCommand(BaseCommand):
    def __init__(self):
        super().__init__()


class InitBatabase(ServiceCommand):
    COMMAND_NAME = "init_db"

    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.INIT_DATABASE_HELP_MSG

    def execute(self, commandArgs=None):
        return Initializer.run()


class InitBooks(ServiceCommand):
    COMMAND_NAME = "init"

    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.INIT_BOOKS_HELP_MSG

    def execute(self, commandArgs=None):
        try:
            for book in g_referenceBooks:
                book.init()
            return True
        except Exception as e:
            _log.debug(e)
            return False


COMMANDS = {
    InitBatabase.COMMAND_NAME: InitBatabase,
    InitBooks.COMMAND_NAME: InitBooks
}
