import socket


def main():
    # Хост и порт сервера
    host = "localhost"
    port = 9999

    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Подключение к серверу
        client_socket.connect((host, port))
        print(f"Server response: {client_socket.recv(1024).decode()}")

        while True:
            # Ввод команды с клавиатуры
            command = input("Enter a command: ")

            # Отправка команды серверу
            client_socket.send(command.encode())

            # Получение ответа от сервера
            data = client_socket.recv(1024)
            print("Server response:", data.decode())

            # Проверка на выход
            if command.lower() == "quit":
                break
    except Exception as e:
        print("Error:", e)
    finally:
        # Закрытие сокета
        client_socket.close()


if __name__ == "__main__":
    main()
