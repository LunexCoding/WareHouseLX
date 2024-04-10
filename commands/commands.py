from .consts import Constants
from .processСonditions import ProcessConditions
from dataStructures.referenceBook import g_referenceBooks
from tools.customExcepions import MissingCommandArgumentException, InvalidCommandFlagException


class FlagsType:
    SINGLE = 0
    WITH_VALUE = 1
    VALUE_WITHOUT_FLAG = 2


class ValueType:
    NONE = 0
    INT = 1
    STRING = 2
    FLOAT = 3


class Command:
    COMMAND_NAME = None

    def __init__(self):
        self.msgHelp = None
        self._allowedFlags = {}
        self._argsWithoutFlagsOrder = []

    def execute(self, commandArgs):
        assert False

    def getHelpMsg(self):
        return self.msgHelp

    def _getArgs(self, argsline):
        args = argsline.split()
        commandArgs = {}
        last = None
        flags = iter(self._argsWithoutFlagsOrder)
        for arg in args:
            try:
                if last is None:
                    if arg in self._allowedFlags:
                        commandArgs[arg] = None
                        if self._allowedFlags[arg] != ValueType.NONE:
                            last = arg
                    else:
                        if "-" in arg:
                            commandArgs[arg] = None
                            last = arg
                        else:
                            last = next(flags)
                            commandArgs[last] = self._convertValue(last, arg)
                            last = None
                else:
                    if "-" in arg:
                        commandArgs[arg] = None
                    else:
                        commandArgs[last] = self._convertValue(last, arg)
                        last = None
            except StopIteration:
                break
        return commandArgs

    def _convertValue(self, flag, arg):
        if flag in self._allowedFlags:
            valueType = self._allowedFlags[flag]
            if valueType == ValueType.INT:
                return int(arg)
            if valueType == ValueType.FLOAT:
                return float(arg)
            return arg
        return arg

    def _checkFlags(self, args):
        invalidFlags = [flag for flag in args if flag not in self._allowedFlags]
        if invalidFlags:
            raise InvalidCommandFlagException(self.__class__.COMMAND_NAME, invalidFlags)
        missingFlags = [flag for flag in self._allowedFlags if args.get(flag) is None]
        if missingFlags:
            raise MissingCommandArgumentException(self.__class__.COMMAND_NAME, missingFlags)


class Help(Command):
    COMMAND_NAME = "help"

    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.HELP_MSG
        self._allowedFlags = None
        self._argsWithoutFlagsOrder = None

    def execute(self, commandName=None):
        if commandName is None:
            return self.msgHelp % "\n".join([f"\t{index}. {command}" for index, command in enumerate(commands, start=1)])
        if commandName in commands:
            return commands[commandName]().getHelpMsg()


class SearchRows(Command):
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
    Help.COMMAND_NAME: Help,
    SearchRows.COMMAND_NAME: SearchRows
}
