from collections import namedtuple

from .pageDataObjContext import PageDataObjContext
from dataStructures.referenceBook import g_usersBook, g_ordersBook, g_machinesBook


PAGE = namedtuple("CONTEXT", ["context", "book"])


class Pages:
    USERS = PAGE(PageDataObjContext, g_usersBook)
    ORDERS = PAGE(PageDataObjContext, g_ordersBook)
    MACHINES = PAGE(PageDataObjContext, g_machinesBook)
