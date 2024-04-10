```python
[10-Apr-24 12:56] -> __main__ -> [DEBUG]: Server listening on localhost:9999
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Connection from ('127.0.0.1', 56125)
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: ff -g 1
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Unknown command: ff
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: help
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Response: Доступные команды:
	1. help
	2. add
Использование:
    help [command]
Пример:
    help add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-f', '-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -f
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-f', '-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -s
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-f', '-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -f 1
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -s 2
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-f'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add 1
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add 2
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -f 1 -s
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -s 2 -f
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-f'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -f -s
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Missing arguments: ['-f', '-s'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -f 1 -s 2
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Response: 3.0
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add 1 2
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Response: 3.0
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -g 1
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Invalid command flag: ['-g'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add -g 1 -h
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Invalid command flag: ['-g', '-h'] for command: add
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: 
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Empty data received, closing connection
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Connection from ('127.0.0.1', 56128)
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: add 1 2
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Response: 3.0
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Received: 
[10-Apr-24 12:58] -> __main__ -> [DEBUG]: Empty data received, closing connection
