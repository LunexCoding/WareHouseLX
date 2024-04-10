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

    def execute(self, commandArgs):
        args = self._getArgs(commandArgs)
        self._checkFlags(args)

        table = args["-t"]
        referenceBook = [book for book in g_referenceBooks if book.table == table][0]
        conditionString = args["-c"]

        conditions = ProcessConditions.process(conditionString.split("|"), referenceBook.columns)
        if len(conditions) == 1:
            conditions = "".join(conditions)
        return referenceBook.searchRowByParams(conditions)


commands = {
    SearchRows.COMMAND_NAME: SearchRows
}
