import socket
import threading

from settingsConfig import g_settingsConfig
from tools.logger import logger
from commands.commands import commands
from consts import Constants
from tools.customExcepions import MissingCommandArgumentException


_log = logger.getLogger(__name__)


class Server:
    def __init__(self):
        # self._host = g_settingsConfig.ServerSettings["host"]
        # self._port = g_settingsConfig.ServerSettings["port"]
        self._host = "localhost"
        self._port = 9999

    def handleClient(self, clientSocket, addr):
        _log.debug(f"Connection from {addr}")
        clientSocket.send(Constants.WELCOME_MESSAGE.encode())

        while True:
            try:
                data = clientSocket.recv(1024)
                if not data:
                    break
                _log.debug(f"Input received: {data.decode()}")

                commandString = data.decode().strip().split()
                command = commandString.pop(0)
                argsCommand = " ".join(commandString)
                threading.Thread(target=self.handleUserInput, args=(clientSocket, command, argsCommand)).start()

            except Exception as e:
                _log.error(f"Error handling client command: {e}")

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

    def run(self):
        # Создаем сокет
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self._host, self._port))
        serverSocket.listen(5)

        _log.debug(f"Server listening on {self._host}:{self._port}")

        while True:
            # Принимаем подключение от клиента
            clientSocket, addr = serverSocket.accept()

            # Запускаем новый поток для обработки клиента
            clientThread = threading.Thread(target=self.handleClient, args=(clientSocket, addr))
            clientThread.start()


if __name__ == "__main__":
    server = Server()
    server.run()
