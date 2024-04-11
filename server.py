import asyncio
import socket
import sys

from tools.logger import logger
from serverConsts import Constants
from tools.jsonTools import JsonTools
from commands.customExcepions import MissingCommandArgumentException, InvalidCommandFlagException
from commands.center import g_commandCenter
from dataStructures.referenceBook import g_referenceBooks


_log = logger.getLogger(__name__)


class Server:
    def __init__(self):
        self.host = "localhost"
        self.port = 9999
        self.running = True
        self.clients = []

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

                asyncio.create_task(self.processCommand(clientSocket, command, argsCommand))

            except asyncio.TimeoutError:
                _log.error("Timeout occurred while receiving data")
                break

        clientSocket.close()
        self.clients.remove((clientSocket, addr))

    async def processCommand(self, clientSocket, command, argsCommand):
        await g_commandCenter.addToExecutionQueue((command, argsCommand))
        result = await g_commandCenter.executeAllCommands()
        if not isinstance(result, (dict, list)):
            clientSocket.send(str(result).encode())
            _log.debug(f"Response: {str(result)}")
        else:
            clientSocket.send(JsonTools.serialize(result).encode())
            _log.debug(f"Response: {JsonTools.serialize(result)}")

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

    async def stop(self):
        _log.debug("Stopping server...")
        self.running = False
        await asyncio.sleep(10)
        _log.debug("Force closing remaining client connections...")
        for clientSocket, addr in self.clients:
            try:
                clientSocket.shutdown(socket.SHUT_RDWR)
                clientSocket.close()
            except Exception as e:
                _log.error(f"Error closing client connection: {e}")

        self.clients.clear()
        _log.debug("Server stopped.")
        sys.exit()


async def main():
    server = Server()

    for book in g_referenceBooks:
        book.init()

    accept_clients_task = asyncio.create_task(server.acceptClients())

    while True:
        command = await asyncio.get_event_loop().run_in_executor(None, input, "Enter command -> ")
        if command.lower() == "stop":
            await server.stop()
            break

    await accept_clients_task
    await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
