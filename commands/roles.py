from collections import namedtuple

ROLE = namedtuple("Role", ["Guest", "User", "Admin"])


class Roles:
    roles = ROLE(0, 1, 2)

    @classmethod
    def getRole(cls, roleStatus):
        try:
            return ROLE._fields[roleStatus]
        except IndexError:
            return ROLE._fields[0]
