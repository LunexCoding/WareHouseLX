import asyncio
from tools.logger import logger
from commands.center import g_commandCenter
from connection import Socket


_log = logger.getLogger(__name__)


class Server:
    def __init__(self):
        self.socket = None

    async def start(self):
        await g_commandCenter.addToExecutionQueue("init")
        await g_commandCenter.executeNextCommand()

        await g_commandCenter.addToExecutionQueue("start")
        result = await g_commandCenter.executeAllCommands()
        if result and isinstance(result, Socket):
            self.socket = result
        else:
            _log.error("Failed to start the server socket.")

        await self.startSocket()

    async def startSocket(self):
        self.socket.acceptClientsTask = asyncio.create_task(self.socket.acceptClients())
        g_commandCenter.executeAllCommandsTask = asyncio.create_task(g_commandCenter.executeAllCommands())

    async def stopSocket(self):
        print("call stopSocket")
        if self.socket:
            await self.socket.stop()
            await g_commandCenter.addToExecutionQueue(("stop", self.socket))
            await g_commandCenter.executeNextCommand()  # Выполнить команду "stop"
            self.socket = None

async def main():
    server = Server()
    await server.start()
    await asyncio.sleep(10)
    await server.stopSocket()


if __name__ == "__main__":
    asyncio.run(main())
