import socket
import threading

from client import Client
from commands.status import COMMAND_STATUS
from tools.jsonTools import JsonTools
from tools.logger import logger
from consts import Constants


_log = logger.getLogger(__name__)


class Socket:
    def __init__(self, commandCenter):
        self.host = "localhost"
        self.port = 9999
        self.running = False
        self.clients = []
        self.commandCenter = commandCenter

    def handleClient(self, clientSocket, addr):
        client = Client(clientSocket, addr)
        self.clients.append(client)
        _log.debug(f"Connection from {addr}")

        while self.running:
            try:
                data = clientSocket.recv(1024)
                data = data.decode().strip()

                if data.strip():
                    _log.debug(f"Received: {data}")
                    self.processCommand(self.clients.index(client), data)

            except Exception as e:
                _log.error(f"Error handling client: {e}")
                break

    def processCommand(self, clientID, command):
        client = self.clients[clientID]
        clientSocket = client.socket

        commandString = command.split()
        commandName = commandString.pop(0)
        argsCommand = " ".join(commandString)
        commandObj = self.commandCenter.searchCommand(commandName)
        if commandObj is not None:
            result = commandObj.execute(argsCommand, client.role, client.isAuthorized)
            result = {
                "Command": command,
                "Status": result[0],
                "Result": result[1]
            }
            if commandObj.COMMAND_NAME == Constants.AUTHORIZATION_COMMAND:
                if client.authorization(result):
                    _log.debug(f"Client is authorized ->  ID<{client.userID}>, fullname: {client.fullname}")
        else:
            _log.error(Constants.COMMAND_NOT_FOUND_MSG.format(commandName))
            result = {
                "Command": command,
                "Status": COMMAND_STATUS.FAILED,
                "Result": Constants.COMMAND_NOT_FOUND_MSG.format(commandName)
            }
        response = JsonTools.serialize(result)
        self.sendToClient(clientSocket, response)

    @staticmethod
    def sendToClient(clientSocket, response):
        clientSocket.send(response.encode())
        _log.debug(f"Response: {response}")

    def start(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.host, self.port))
        serverSocket.listen(5)
        self.running = True
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
        for client in self.clients:
            try:
                client.socket.shutdown(socket.SHUT_RDWR)
                client.socket.close()
            except Exception as e:
                _log.error(f"Error closing client connection: {e}")

        self.clients.clear()
        _log.debug("Socket stopped.")
