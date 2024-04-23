class ACCESS_LEVEL:
    GUEST = 0
    USER = 1
    ADMIN = 2


class ROLES:
    GUEST = 0
    USER = 1
    ADMIN = 2

    @classmethod
    def getRoleStatus(cls, roleName):
        try:
            return getattr(cls, roleName.upper())
        except AttributeError:
            return cls.GUEST
