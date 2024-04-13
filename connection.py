import socket
import threading

from tools.jsonTools import JsonTools
from tools.logger import logger
from consts import Constants


_log = logger.getLogger(__name__)


class Socket:
    def __init__(self, commandCenter):
        self.host = "localhost"
        self.port = 9999
        self.running = True
        self.clients = []
        self.commandCenter = commandCenter

    def handleClient(self, clientSocket, addr):
        self.clients.append((clientSocket, addr))
        _log.debug(f"Connection from {addr}")

        while self.running:
            try:
                data = clientSocket.recv(1024)
                data = data.decode().strip()

                if data.strip():
                    _log.debug(f"Received: {data}")

                    thread = threading.Thread(target=self.processCommand, args=(clientSocket, data))
                    thread.start()
                    thread.join()

            except Exception as e:
                _log.error(f"Error handling client: {e}")
                break

    def processCommand(self, clientSocket, command):
        commandString = command.split()
        commandName = commandString.pop(0)
        argsCommand = " ".join(commandString)
        commandObj = self.commandCenter.searchCommand(commandName)
        if commandObj is not None:
            result = commandObj.execute(argsCommand)
            if not isinstance(result, (dict, list)):
                result = [result]
            result = {
                "Command": command,
                "Result": result
            }
            response = JsonTools.serialize(result)
            clientSocket.send(response.encode())
            _log.debug(f"Response: {response}")
        else:
            clientSocket.send(str(None).encode())
            _log.error(Constants.COMMAND_NOT_FOUND_MSG.format(commandName))
            _log.debug(f"Response: {None}")

    def start(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.host, self.port))
        serverSocket.listen(5)
        _log.debug(f"Server listening on {self.host}:{self.port}")

        while self.running:
            try:
                clientSocket, addr = serverSocket.accept()
                threading.Thread(target=self.handleClient, args=(clientSocket, addr)).start()
            except Exception as e:
                _log.error(f"Error accepting client: {e}")

        _log.debug("Socket stopped.")

    def stop(self):
        _log.debug("Stopping socket...")
        self.running = False
        for clientSocket, addr in self.clients:
            try:
                clientSocket.shutdown(socket.SHUT_RDWR)
                clientSocket.close()
            except Exception as e:
                _log.error(f"Error closing client connection: {e}")

        self.clients.clear()
        _log.debug("Socket stopped.")
