from collections import namedtuple

from dataStructures.order import Order
from .order.infoWithEditContext import InfoWithEditOrderContext


CONTEXT = namedtuple("CONTEXT", ["dataObj", "contextInstance"])


class INFO_CONTEXTS:
    ORDER = CONTEXT(Order, InfoWithEditOrderContext)

    @classmethod
    def getContextByInstance(cls, instance):
        for context in cls.__dict__.values():
            if isinstance(context, CONTEXT):
                if context.dataObj == instance:
                    return context
        return None
