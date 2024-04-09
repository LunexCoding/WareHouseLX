import asyncio
import socket
import threading


class CommandClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = None
        self.responses = []
        self.responseLock = threading.Lock()  # Lock для защиты доступа к переменной responses
        self.listenerThread = None
        self.stopListenerThread = False  # Флаг для остановки потока прослушивания
        self.connectionClosed = False  # Флаг для указания закрытия соединения

    async def connect(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.connect, (self.host, self.port))

        # Отдельный поток для прослушивания сервера
        self.listenerThread = threading.Thread(target=self.listenServer)
        self.listenerThread.start()

    def listenServer(self):
        while not self.connectionClosed and not self.stopListenerThread:  # Добавлено условие выхода из цикла
            try:
                # Устанавливаем таймаут для сокета
                self.clientSocket.settimeout(1)  # Задаем таймаут 1 секунду
                data = self.clientSocket.recv(1024)
                if not data:
                    self.connectionClosed = True
                    break

                with self.responseLock:
                    self.responses.append(data.decode())
            except socket.timeout:
                pass  # Игнорируем исключение socket.timeout
            except Exception as e:
                print("Error occurred while receiving response:", e)
                self.connectionClosed = True
                break

        if self.clientSocket:
            self.clientSocket.close()

    async def send_command(self, command):
        if not self.clientSocket:
            raise ConnectionError("Client is not connected. Call connect() method first.")
        await asyncio.get_event_loop().run_in_executor(None, self.clientSocket.send, command.encode())

    def close(self):
        self.connectionClosed = True
        self.stopListenerThread = True  # Устанавливаем флаг для остановки потока
        if self.listenerThread:
            self.listenerThread.join()
        if self.clientSocket:
            self.clientSocket.close()
            self.clientSocket = None


async def main():
    client = CommandClient('localhost', 9999)
    await client.connect()

    # Список команд для отправки
    commands = ["add 1 2", "add 3 4", "add 10 5"]

    # Отправляем каждую команду и ожидаем ответа
    for cmd in commands:
        await client.send_command(cmd)
        await asyncio.sleep(0.1)

    # Получаем ответы от сервера
    with client.responseLock:
        responses = client.responses

    print("Responses from server:", responses)

    # Закрываем соединение
    client.close()

# Запускаем основную функцию
asyncio.run(main())
