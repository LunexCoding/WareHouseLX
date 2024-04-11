import asyncio

from commands.service import commands as serviceCommands
from commands.client import commands as clientCommands


class CommandCenter:
    def __init__(self):
        self.serviceCommands = serviceCommands
        self.clientCommands = clientCommands
        self.executionQueue = asyncio.Queue()

    async def addToExecutionQueue(self, command):
        await self.executionQueue.put(command)

    async def executeNextCommand(self):
        if not self.executionQueue.empty():
            nextCommand = await self.executionQueue.get()
            if isinstance(nextCommand, tuple):
                command, args = nextCommand
                if command in self.serviceCommands:
                    command = self.serviceCommands[command]
                    return command.execute(args)
                elif command in self.clientCommands:
                    command = self.clientCommands[command]()
                    return command.execute(args)
        return False

    async def executeAllCommands(self):
        while not self.executionQueue.empty():
            return await self.executeNextCommand()


g_commandCenter = CommandCenter()
