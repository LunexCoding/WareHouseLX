from pathlib import Path

from tools.fileSystemExceptions import (
    PathExistsException,
    PathExistsAsFileException
)


class FileSystem:
    @staticmethod
    def exists(path):
        return Path(path).exists()

    @staticmethod
    def makeDir(path, recreate=False):
        path = Path(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        if path.exists() and recreate is False:
            raise PathExistsException(path)
        path.mkdir(exist_ok=recreate)
        return True
