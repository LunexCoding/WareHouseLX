import socket
import threading

from client import Client
from commands.status import COMMAND_STATUS
from tools.logger import logger
from commands.consts import Constants as CMDConstants
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
        _log.debug(f"Connection from Addr<{addr}>")

        while self.running:
            try:
                data = clientSocket.recv(1024)

                if not data:
                    _log.debug(f"Client {Constants.LOG_USER_INFO_STRING.format(client.userID, client.fullname)} disconnected")
                    self.clients.remove(client)
                    break

                data = data.decode("utf-8").strip()

                if data.strip():
                    _log.debug(f"Received {Constants.LOG_USER_INFO_STRING.format(client.userID, client.fullname)} data: {data}")
                    self.processCommand(self.clients.index(client), data)
            except ConnectionResetError:
                _log.error(f"Client {Constants.LOG_USER_INFO_STRING.format(client.userID, client.fullname)} terminated an existing connection")
                break
            except Exception as e:
                _log.error(f"Error handling client {Constants.LOG_USER_INFO_STRING.format(client.userID, client.fullname)} {e}", exc_info=True)
                break

    def processCommand(self, clientID, command):
        client = self.clients[clientID]
        commandString = command.split(CMDConstants.SERVICE_SYMBOL)
        commandID = int(commandString.pop(0))
        argsCommand = " ".join(commandString).replace(CMDConstants.SERVICE_SYMBOL, " ")
        commandObj, args = self.commandCenter.searchCommand(commandID)
        if commandObj is not None:
            if args is not None:
                argsCommand += args
            result = commandObj.execute(client, argsCommand)
            status, records = result[0], result[1]
            if records is not None:
                if isinstance(records, list):
                    data = "|".join(CMDConstants.SERVICE_SYMBOL.join(map(str, record.values())) for record in records)
                else:
                    data = records
                response = Constants.RESPONSE_STRING.format(commandID, status, data)
            else:
                data = None
                response = Constants.RESPONSE_STRING.format(commandID, status, data)
        else:
            _log.error(f"{Constants.LOG_USER_INFO_STRING.format(client.addr, client.userID, client.fullname)} {Constants.COMMAND_NOT_FOUND_MSG.format(commandID)}")
            response = Constants.RESPONSE_STRING.format(commandID, COMMAND_STATUS.FAILED, Constants.COMMAND_NOT_FOUND_MSG.format(commandID))
        self.sendToClient(client, response)

    @staticmethod
    def sendToClient(client, response):
        clientSocket = client.socket
        clientSocket.send(response.encode("utf-8"))
        _log.debug(f"Response {Constants.LOG_USER_INFO_STRING.format(client.userID, client.fullname)} data: {response}")

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
                _log.error(f"Error closing client {Constants.LOG_USER_INFO_STRING.format(client.addr, client.userID, client.fullname)} {e}")

        self.clients.clear()
        _log.debug("Socket stopped.")
