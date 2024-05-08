import socket

from settingsConfig import g_settingsConfig


class _Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = None
        self.responses = []

    def init(self):
        self.connect()

    def connect(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.host, self.port))

    def sendCommand(self, command):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call the connect() method first.")
        self.clientSocket.sendall(str(command).encode())

    def receiveResponse(self):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call the connect() method first.")
        receivedData = ""
        while True:
            response = self.clientSocket.recv(1024).decode()
            if response[-1] != " ":
                receivedData += response
                break
            receivedData += response
        return receivedData

    def sendAndReceiveSync(self, command):
        self.sendCommand(command)
        response = self.receiveResponse()
        return response.split()

    def sendAndReceiveAsync(self, commands):
        self.clearResponses()

        for command in commands:
            response = self.sendAndReceiveSync(command)
            self.responses.append(response)

        return self.responses

    def clearResponses(self):
        self.responses.clear()


g_socket = _Socket(
    g_settingsConfig.ServerSettings["host"],
    g_settingsConfig.ServerSettings["port"]
)
