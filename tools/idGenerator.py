import uuid


class IDGenerator:
    @staticmethod
    def getID():
        return str(uuid.uuid4())


g_IDGenerator = IDGenerator()
