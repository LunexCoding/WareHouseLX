from collections import namedtuple

from dataStructures.dataObjs.user import User
from dataStructures.dataObjs.order import Order
from dataStructures.dataObjs.machine import Machine
from .user.infoWithEditContext import InfoWithEditUserContext
from .order.infoWithEditContext import InfoWithEditOrderContext
from .machine.infoWithEditContext import InfoWithEditMachineContext


CONTEXT = namedtuple("CONTEXT", ["dataObj", "contextInstance"])


class INFO_CONTEXTS:
    USER = CONTEXT(User, InfoWithEditUserContext)
    ORDER = CONTEXT(Order, InfoWithEditOrderContext)
    MACHINE = CONTEXT(Machine, InfoWithEditMachineContext)

    @classmethod
    def getContextByInstance(cls, instance):
        for context in cls.__dict__.values():
            if isinstance(context, CONTEXT):
                if context.dataObj == instance:
                    return context
        return None
