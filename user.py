from commands.roles import ROLES


class User:
    def __init__(self):
        self._userID = None
        self._login = None
        self._fullname = None
        self._role = ROLES.GUEST

    def authorization(self, login, password):
        ...

    @property
    def userID(self):
        return self._userID

    @property
    def login(self):
        return self._login

    @property
    def fullname(self):
        return self._fullname
