from .consts import Constants
from tools.customExcepions import MissingCommandArgumentException


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
            if last is None:
                if arg in self._allowedFlags:
                    commandArgs[arg] = None
                    if self._allowedFlags[arg] != ValueType.NONE:
                        last = arg
                else:
                    last = next(flags)
                    commandArgs[last] = self._convertValue(last, arg)
                    last = None
            else:
                commandArgs[last] = self._convertValue(last, arg)
                last = None
        return commandArgs

    def _convertValue(self, flag, arg):
        valueType = self._allowedFlags[flag]
        if valueType == ValueType.INT:
            return int(arg)
        if valueType == ValueType.FLOAT:
            return float(arg)
        return arg

    def _checkFlags(self, args):
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


class Addition(Command):
    COMMAND_NAME = "add"

    def __init__(self):
        super().__init__()
        self.msgHelp = Constants.ADDITION_HELP_MSG
        self._allowedFlags = {
            "-f": ValueType.FLOAT,
            "-s": ValueType.FLOAT
        }
        self._argsWithoutFlagsOrder = ["-f", "-s"]

    def execute(self, commandArgs):
        args = self._getArgs(commandArgs)

        self._checkFlags(args)

        first = args["-f"]
        second = args["-s"]
        return first + second


commands = {
    Help.COMMAND_NAME: Help,
    Addition.COMMAND_NAME: Addition
}
