import socket
import json

from database.tables import DatabaseTables


class ClientSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = None
        self.responses = []

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
        receivedData = self.clientSocket.recv(1024)
        response = receivedData.decode()
        return json.loads(response)

    def sendAndReceive(self, command):
        self.sendCommand(command)
        response = self.receiveResponse()
        return response

    def sendAndReceiveInThreads(self, commands):
        self.clearResponses()

        for command in commands:
            response = self.sendAndReceive(command)
            self.responses.append(response)

        return self.responses

    def clearResponses(self):
        self.responses.clear()


if __name__ == "__main__":
    host = 'localhost'
    port = 9999

    client1 = ClientSocket(host, port)
    client2 = ClientSocket(host, port)

    client1.connect()
    client2.connect()

    commands1 = [
        "long_run",
        f"search {DatabaseTables.USERS} RoleID=2",
        f"search {DatabaseTables.USERS} RoleID=2|ID<3",
        "add",
        "authorization admin admin",
        f"search {DatabaseTables.USERS} RoleID=2",
    ]
    commands2 = [
        "long_run",
        f"search {DatabaseTables.USERS} RoleID=2",
        f"search {DatabaseTables.USERS} RoleID=2|ID<3",
        "add",
        "authorization user user",
        f"search {DatabaseTables.USERS} RoleID=2",
    ]


    responses1 = client1.sendAndReceiveInThreads(commands1)
    responses2 = client2.sendAndReceiveInThreads(commands2)

    sortedResponses1 = [response for response in responses1]
    sortedResponses2 = [response for response in responses2]

    print("Responses from clientApp 1:", sortedResponses1)
    print("Responses from clientApp 2:", sortedResponses2)

