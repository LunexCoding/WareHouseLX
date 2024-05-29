from collections import namedtuple

from dataStructures.workshop import Workshop
from dataStructures.order import Order
from .order.infoWithEditContext import InfoWithEditOrderContext
from .workshop.infoWithEditContext import InfoWithEditWorkshopContext


CONTEXT = namedtuple("CONTEXT", ["dataObj", "contextInstance"])


class INFO_CONTEXTS:
    WORKSHOP = CONTEXT(Workshop, InfoWithEditWorkshopContext)
    ORDER = CONTEXT(Order, InfoWithEditOrderContext)

    @classmethod
    def getContextByInstance(cls, instance):
        for context in cls.__dict__.values():
            if isinstance(context, CONTEXT):
                if context.dataObj == instance:
                    return context
        return None
