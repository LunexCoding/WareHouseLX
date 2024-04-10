import asyncio
import socket

from clientConsts import Constants
from database.tables import DatabaseTables


class CommandClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = None

    async def connect(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.connect, (self.host, self.port))

    async def sendCommand(self, command):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call connect() method first.")
        await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.sendall, command.encode())

    async def receiveResponse(self):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call connect() method first.")
        receivedData = b""
        self.clientSocket.settimeout(1)
        while True:
            try:
                dataChunk = self.clientSocket.recv(1024)
                if not dataChunk:
                    break
                receivedData += dataChunk
            except socket.timeout:
                break
        return receivedData.decode()

    async def sendCommandsAndReceiveResponses(self, commands):
        await self.connect()
        responses = []

        for command in commands:
            await self.sendCommand(command)
            response = await self.receiveResponse()
            if any(msg in response for msg in [Constants.UNKNOWN_COMMAND_MSG, Constants.MISSING_COMMAND_ARGUMENT_MSG, Constants.INVALID_COMMAND_FLAG_MSG]):
                responses.append(None)
            else:
                responses.append(response)

        self.clientSocket.close()
        return responses

    async def sendCommandAndReceiveResponse(self, command):
        await self.connect()
        await self.sendCommand(command)
        response = await self.receiveResponse()
        if any(msg in response for msg in [Constants.UNKNOWN_COMMAND_MSG, Constants.MISSING_COMMAND_ARGUMENT_MSG, Constants.INVALID_COMMAND_FLAG_MSG]):
            return None

        self.clientSocket.close()
        return response


async def main():
    client = CommandClient('localhost', 9999)

    commands = [
        f"search {DatabaseTables.USERS} RoleID=2",
        f"search {DatabaseTables.USERS} RoleID=2|ID<3"
    ]
    responses = await client.sendCommandsAndReceiveResponses(commands)
    for index, response in enumerate(responses, start=1):
        print(f"{index} | {response}")

    response = await client.sendCommandAndReceiveResponse(f"search {DatabaseTables.USERS} RoleID=2|ID<3")
    print(response)


asyncio.run(main())
