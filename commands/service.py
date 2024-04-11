from .command import BaseCommand
from tools.logger import logger


_log = logger.getLogger(__name__)


class ServiceCommand(BaseCommand):
    def __init__(self):
        super().__init__()


class StartSocket(ServiceCommand):
    COMMAND_NAME = "start"


class StopSocket(ServiceCommand):
    COMMAND_NAME = "stop"


commands = {
    StartSocket.COMMAND_NAME: StartSocket,
    StopSocket.COMMAND_NAME: StopSocket
}