from .service import commands as serviceCommands
from .client import commands as clientCommands
from tools.logger import logger


_log = logger.getLogger(__name__)


class CommandCenter:
    def __init__(self):
        self.commands = {**serviceCommands, **clientCommands}

    def searchCommand(self, command):
        if command in self.commands:
            return self.commands[command]()
        return None


g_commandCenter = CommandCenter()
