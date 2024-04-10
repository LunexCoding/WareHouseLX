from .command import BaseCommand


class ServiceCommand(BaseCommand):
    def __init__(self):
        super().__init__()


class StartSocket(ServiceCommand):
    COMMAND_NAME = "stert"


class StopSocket(ServiceCommand):
    COMMAND_NAME = "stop"


commands = {
    StartSocket.COMMAND_NAME: StartSocket,
    StopSocket.COMMAND_NAME: StopSocket
}
