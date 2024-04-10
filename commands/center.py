import asyncio

from .client import commands as clientCommands
from .service import commands as serviceCommands


class CommandCenter:
    def __init__(self):
        self.serviceCommands = serviceCommands
        self.clientCommands = clientCommands
        self.executionQueue = asyncio.Queue()

    async def addToExecutionQueue(self, *commands):
        for command in commands:
            await self.executionQueue.put(command)

    async def executeNextCommand(self):
        if not self.executionQueue.empty():
            next_command = await self.executionQueue.get()
            result = await next_command.execute()
            return result

    async def executeAllCommands(self):
        while not self.executionQueue.empty():
            result = await self.executeNextCommand()
            if result is not None:
                return result


g_commandCenter = CommandCenter()
