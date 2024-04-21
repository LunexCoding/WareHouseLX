class BasePathException(OSError):
    def __init__(self, path):
        self._path = path


class PathExistsException(BasePathException):
    def __str__(self):
        return f"Path <{self._path}> exists"


class PathExistsAsFileException(BasePathException):
    def __str__(self):
        return f"Path <{self._path}> exists as file, not as a directory"
