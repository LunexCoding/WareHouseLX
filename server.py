import socket
import threading
from settingsConfig import g_settingsConfig
from tools.logger import logger
from tools.jsonTools import JsonTools
from commands.commands import commands
from consts import Constants
from tools.customExcepions import MissingCommandArgumentException

_log = logger.getLogger(__name__)

class Server:
    def __init__(self):
        self._host = "localhost"
        self._port = 9999
        self._serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serverSocket.bind((self._host, self._port))
        self._clients = []
        self._running = True

    def handleClient(self, clientSocket, addr):
        _log.debug(f"Connection from {addr}")
        clientSocket.send(Constants.WELCOME_MESSAGE.encode())

        while self._running:
            try:
                data = clientSocket.recv(1024)
                if not data:
                    _log.debug("Empty data received, closing connection")
                    break

                commandString = data.decode().strip().split()
                command = commandString.pop(0)
                argsCommand = " ".join(commandString)
                self.handleUserInput(clientSocket, command, argsCommand)

            except Exception as e:
                _log.error(f"Error handling client command: {e}")
                break

        clientSocket.close()

    def handleUserInput(self, clientSocket, command, argsCommand):
        if command == "help" and len(argsCommand) == 0:
            argsCommand = None
        if command in commands:
            try:
                data = commands[command]().execute(argsCommand)
                if data is not None:
                    if not isinstance(data, (dict, list)):
                        clientSocket.send(str(data).encode())
                    else:
                        clientSocket.send(JsonTools.serialize(data).encode())
            except MissingCommandArgumentException as e:
                _log.debug(e)
                clientSocket.send(str(e).encode())
        else:
            errorMessage = Constants.UNKNOWN_COMMAND_MSG.format(command)
            _log.debug(errorMessage)
            clientSocket.send(errorMessage.encode())

    def acceptClients(self):
        while self._running:
            try:
                clientSocket, addr = self._serverSocket.accept()
                clientThread = threading.Thread(target=self.handleClient, args=(clientSocket, addr))
                clientThread.start()
                self._clients.append((clientSocket, addr))
            except OSError as e:
                if self._running:
                    _log.error(f"Error accepting client: {e}")

    def stop(self):
        _log.debug("Stopping server...")
        self._running = False
        self._serverSocket.close()

    def run(self):
        self._serverSocket.listen(5)
        _log.debug(f"Server listening on {self._host}:{self._port}")
        acceptThread = threading.Thread(target=self.acceptClients)
        acceptThread.start()


if __name__ == "__main__":
    server = Server()
    server.run()

    while True:
        command = input("Enter command: ")
        if command.lower() == "stop":
            server.stop()
            break
