import asyncio
import socket
from concurrent.futures import ThreadPoolExecutor


# Функция для отправки команды с использованием синхронного сокета
def sendCommandSync(clientSocket, command):
    clientSocket.send(command.encode())


# Функция для приема ответа с использованием синхронного сокета
def receiveResponseSync(clientSocket):
    return clientSocket.recv(1024)


async def main():
    host = "localhost"
    port = 9999
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))

    try:
        commands = [
            "add",
            "add 1",
            "add 1 2",
            "add -f",
            "add -f 1",
            "add -f 1 -s",
            "add -f 1 -s 2"
        ]

        # Создаем пул потоков для выполнения операций в другом потоке
        with ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()

            # Отправляем каждую команду по очереди
            for command in commands:
                # Отправляем команду
                await loop.run_in_executor(executor, sendCommandSync, clientSocket, command)

                # Получаем ответ
                response = await loop.run_in_executor(executor, receiveResponseSync, clientSocket)
                print("Server response:", response.decode())

    except Exception as e:
        print("Error:", e)
    finally:
        # Закрываем сокет после завершения
        clientSocket.close()


if __name__ == "__main__":
    asyncio.run(main())
