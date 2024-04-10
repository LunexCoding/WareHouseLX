class MissingCommandArgumentException(Exception):
    def __init__(self, command, arguments):
        self.command = command
        self.arguments = arguments

    def __str__(self):
        return f"Missing arguments: {self.arguments} for command: {self.command}"


class InvalidCommandFlagException(Exception):
    def __init__(self, command, flags):
        self.command = command
        self.flag = flags

    def __str__(self):
        return f"Invalid command flag: {self.flag} for command: {self.command}"
