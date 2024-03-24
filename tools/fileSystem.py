from pathlib import Path

from tools.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)


class FileSystem:
    @staticmethod
    def exists(path):
        return Path(path).exists()

    @staticmethod
    def makeDir(path, recreate=False):
        path = Path(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if (path.exists() and recreate is False):
            raise PathExistsException(path)
        path.mkdir(exist_ok=recreate)
        return True

    @staticmethod
    def makeDirs(path, recreate=False):
        path = Path(path)
        if (path.exists() and Path(path).is_file()):
            raise PathExistsAsFileException(path)
        if (path.exists() and recreate is False):
            raise PathExistsException(path)
        path.mkdir(parents=True, exist_ok=recreate)
        return True

    @staticmethod
    def remove(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        path.unlink()
        return True

    @staticmethod
    def removeDir(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if not self.isEmpty(path):
            raise IsNotEmptyException(path)
        path.rmdir()
        return True

    @classmethod
    def removeTree(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                cls.removeTree(child)
        path.rmdir()
        return True
