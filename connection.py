import socket
import json

from settingsConfig import g_settingsConfig
from tools.tables import DatabaseTables


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
        self.clientSocket.sendall(command.encode())

    def receiveResponse(self):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call the connect() method first.")
        receivedData = ""
        while True:
            response = self.clientSocket.recv(1024).decode()
            if response[-1] == "}":
                receivedData += response
                break
            receivedData += response
        return json.loads(receivedData)

    def sendAndReceiveSync(self, command):
        self.sendCommand(command)
        response = self.receiveResponse()
        return response

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


if __name__ == "__main__":
    host = 'localhost'
    port = 9999

    client1 = _Socket(host, port)
    client2 = _Socket(host, port)

    client1.connect()
    client2.connect()

    commands1 = [
        "authorization admin admin",
        f"add {DatabaseTables.USERS} [*] [test,test,2,test]",
        f"search {DatabaseTables.USERS} RoleID=2"
    ]
    commands2 = [
        "authorization user user",
        f"add {DatabaseTables.USERS} [*] [test1,test1,2,test1]",
        f"search {DatabaseTables.USERS} RoleID=2"
    ]

    responses1 = client1.sendAndReceiveAsync(commands1)
    responses2 = client2.sendAndReceiveAsync(commands2)

    sortedResponses1 = [response for response in responses1]
    sortedResponses2 = [response for response in responses2]

    print("Responses from clientApp 1:", sortedResponses1)
    print("Responses from clientApp 2:", sortedResponses2)

