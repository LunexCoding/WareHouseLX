import socket

from consts import Constants
from tools.logger import logger
from settingsConfig import g_settingsConfig


_log = logger.getLogger(__name__)


class _Socket:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._clientSocket = None
        self._responses = []

    def init(self):
        self.connect()

    def connect(self):
        self._clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._clientSocket.connect((self._host, self._port))
        _log.debug(f"Connected to server {self._host}:{self._port}")

    def sendCommand(self, command):
        if not self._clientSocket:
            raise ConnectionError(Constants.CLIENT_IS_NOT_CONNECTED_MSG)
        self._clientSocket.sendall(str(command).encode())
        _log.debug(Constants.SENT_MSG.format(command))

    def receiveResponse(self):
        if not self._clientSocket:
            raise ConnectionError(Constants.CLIENT_IS_NOT_CONNECTED_MSG)
        receivedData = ""
        while True:
            response = self._clientSocket.recv(1024).decode()
            if response[-1] != " ":
                receivedData += response
                break
            receivedData += response
        return receivedData

    def sendAndReceiveSync(self, command):
        self.sendCommand(command)
        response = self.receiveResponse()
        _log.debug(Constants.RECEIVED_MSG.format(response))
        return response.split()

    def sendAndReceiveAsync(self, commands):
        self.clearResponses()
        try:
            for command in commands:
                response = self.sendAndReceiveSync(command)
                self._responses.append(response)
            if len(commands) == 1:
                return self._responses[0]
            return self._responses
        except OSError:
            return None

    def clearResponses(self):
        self._responses.clear()

    def checkConnection(self):
        try:
            self._clientSocket.settimeout(1)
            self._clientSocket.connect((self._host, self._port))
            return True
        except Exception:
            return False


g_socket = _Socket(
    g_settingsConfig.ServerSettings["host"],
    g_settingsConfig.ServerSettings["port"]
)
