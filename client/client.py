import socket
import json

from database.tables import DatabaseTables
from clientConsts import Constants


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
        if Constants.COMMAND_FAILED in response:
            return None
        return json.loads(response)

    def sendAndReceive(self, command):
        self.sendCommand(command)
        response = self.receiveResponse()
        return response

    def sendAndReceiveInThreads(self, commands):
        self.clearResponses()

        for command in commands:
            response = self.sendAndReceive(command)
            if response is None:
                self.responses.append(
                    {
                        "Command": command,
                        "Result": None
                    }
                )
            else:
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

    commands = [
        "long_run",
        f"search {DatabaseTables.USERS} RoleID=2",
        f"search {DatabaseTables.USERS} RoleID=2|ID<3",
        "add"
    ]

    for _ in range(2):
        responses1 = client1.sendAndReceiveInThreads(commands)
        responses2 = client2.sendAndReceiveInThreads(commands)

        sorted_responses1 = [response["Result"] for response in responses1]
        sorted_responses2 = [response["Result"] for response in responses2]

        print("Responses from client 1:", sorted_responses1)
        print("Responses from client 2:", sorted_responses2)
        print()
