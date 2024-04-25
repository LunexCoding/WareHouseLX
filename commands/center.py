from connection import g_socket


class _CommandCenter:
    @staticmethod
    def execute(commands):
        if not isinstance(commands, list):
            return g_socket.sendAndReceiveAsync([commands])[0]
        return g_socket.sendAndReceiveAsync(commands)


g_commandCenter = _CommandCenter()
