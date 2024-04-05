class MissingCommandArgumentException(Exception):
    def __init__(self, command, args):
        self.command = command
        self.args = args

    def __str__(self):
        return f"Missing arguments: {self.args} for command: {self.command}"
