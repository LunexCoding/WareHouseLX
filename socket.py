import asyncio
import socket

from commands.center import g_commandCenter
from tools.logger import logger


_log = logger.getLogger(__name__)


class Socket:
    def __init__(self, command_center):
        self.host = "localhost"
        self.port = 9999
        self.running = True
        self.clients = []
        self.command_center = command_center

    async def handleClient(self, clientSocket, addr):
        self.clients.append((clientSocket, addr))
        _log.debug(f"Connection from {addr}")

        while self.running:
            try:
                data = await asyncio.get_event_loop().sock_recv(clientSocket, 1024)
                _log.debug(f"Received: {data.decode()}")
                if not data:
                    _log.debug("Empty data received, closing connection")
                    break

                commandString = data.decode().strip().split()
                command = commandString.pop(0)
                argsCommand = " ".join(commandString)

                await self.command_center.addToExecutionQueue(command, argsCommand)

            except asyncio.TimeoutError:
                _log.error("Timeout occurred while receiving data")
                break

        clientSocket.close()
        self.clients.remove((clientSocket, addr))

    async def acceptClients(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.host, self.port))
        serverSocket.listen(5)
        _log.debug(f"Server listening on {self.host}:{self.port}")

        while self.running:
            try:
                clientSocket, addr = await asyncio.get_event_loop().sock_accept(serverSocket)
                asyncio.create_task(self.handleClient(clientSocket, addr))
            except Exception as e:
                _log.error(f"Error accepting client: {e}")

        _log.debug("Server stopped.")


async def main():
    server = Socket(g_commandCenter)

    accept_clients_task = asyncio.create_task(server.acceptClients())
    command_processing_task = asyncio.create_task(g_commandCenter.executeAllCommands())

    await asyncio.gather(accept_clients_task, command_processing_task)


if __name__ == "__main__":
    asyncio.run(main())
