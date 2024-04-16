import time

from .command import BaseCommand, ValueType
from .processСonditions import ProcessConditions
from dataStructures.referenceBook import g_referenceBooks


class ClientCommand(BaseCommand):
    def __init__(self):
        super().__init__()


class SearchRows(ClientCommand):
    COMMAND_NAME = "search"

    def __init__(self):
        super().__init__()
        self.msgHelp = None
        self._allowedFlags = {
            "-t": ValueType.STRING,
            "-c": ValueType.STRING
        }
        self._argsWithoutFlagsOrder = ["-t", "-c"]

    def execute(self, commandArgs=None):
        args = self._getArgs(commandArgs)
        if self._checkFlags(args):

            table = args["-t"]
            referenceBook = [book for book in g_referenceBooks if book.table == table][0]
            conditionString = args["-c"]

            conditions = ProcessConditions.process(conditionString.split("|"), referenceBook.columns)
            if len(conditions) == 1:
                conditions = "".join(conditions)
            data = referenceBook.searchRowByParams(conditions)
            return data
        return None


class LongRunningCommand(ClientCommand):
    COMMAND_NAME = "long_run"

    def __init__(self):
        super().__init__()
        self.msgHelp = None

    def execute(self, commandArgs=None):
        # Имитация долгой работы на 10 секунд
        start_time = time.time()
        while time.time() - start_time < 10:
            pass
        return True


commands = {
    SearchRows.COMMAND_NAME: SearchRows,
    LongRunningCommand.COMMAND_NAME: LongRunningCommand
}
