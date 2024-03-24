from .database import databaseSession


class DatabasePipeline:
    def __init__(self):
        self.__operations = []

    def addOperation(self, operation, data=None):
        self.__operations.append([operation, data])

    def run(self):
        with databaseSession as db:
            for operationData in self.__operations:
                operation, data = operationData[0], operationData[1]
                if data is not None:
                    db.execute(operation, data)
                else:
                    db.execute(operation)
        self.__clear()

    def __clear(self):
        self.__operations.clear()
