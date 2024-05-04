from customtkinter import CTkFrame, CTkLabel

from ui.contexts.consts import Constants

from .markup import MARCUP, TYPES_UI_MARKUP
from .widget import BaseWidget


class UserInfoWidget(BaseWidget):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.userFrame = CTkFrame(parent)
        self.userRoleLabel = CTkLabel(self.userFrame, text=user.role, font=Constants.FONT)
        self.userFullnameLabel = CTkLabel(self.userFrame, text=user.fullname, font=Constants.FONT)
        self._uiElements.append(MARCUP(element=self.userFrame, type=TYPES_UI_MARKUP.GRID, padx=10, pady=10))
        self._uiElements.append(MARCUP(element=self.userRoleLabel, type=TYPES_UI_MARKUP.PACK, padx=10, pady=10))
        self._uiElements.append(MARCUP(element=self.userFullnameLabel, type=TYPES_UI_MARKUP.PACK, row=0, column=0, padx=10, pady=10))
        self.show()
