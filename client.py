import asyncio
import socket

class CommandClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = None

    async def connect(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.connect, (self.host, self.port))

    async def sendCommand(self, command):
        await self.sendCommandSync(command)

    async def sendCommandSync(self, command):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call connect() method first.")
        await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.send, command.encode())

    async def receiveResponse(self):
        return await self.receiveResponseSync()

    async def receiveResponseSync(self):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call connect() method first.")
        return await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.recv, 1024)

    async def sendAndReceive(self, command):
        await self.sendCommand(command)
        response = await self.receiveResponse()
        return response.decode()

    def close(self):
        if self.clientSocket:
            self.clientSocket.close()
            self.clientSocket = None


# async def send_multiple_commands():
#     host = "localhost"
#     port = 9999
#
#     commands = [
#         "add",
#         "add 1",
#         "add 1 2",
#         "add -f",
#         "add -f 1",
#         "add -f 1 -s",
#         "add -f 1 -s 2"
#     ]
#
#     client = CommandClient(host, port)
#     await client.connect()
#
#     for command in commands:
#         response = await client.sendAndReceive(command)
#         print(f"Command: {command} | Response: {response}")
#
#     client.close()
#
# asyncio.run(send_multiple_commands())