from customtkinter import CTkButton, CTkFrame, E

from commands.roles import Roles, RolesInt
from ui.contexts.consts import Constants
from .markup import MARCUP, TYPES_UI_MARKUP
from .widget import BaseWidget


class CommandButtonsWidget(BaseWidget):
    def __init__(self, master, user, commands):
        super().__init__(master)
        self.buttonFrame = CTkFrame(master)
        self.buttonCreate = CTkButton(self.buttonFrame, text=Constants.BUTTON_CREATE, font=Constants.FONT, command=commands["create"])
        self.buttonSearch = CTkButton(self.buttonFrame, text=Constants.BUTTON_SEARCH, font=Constants.FONT, command=commands["search"])
        self.buttonRemove = CTkButton(self.buttonFrame, text=Constants.BUTTON_DELETE, font=Constants.FONT, command=commands["remove"])
        self._uiElements.append(MARCUP(element=self.buttonFrame, type=TYPES_UI_MARKUP.GRID, row=0, column=2, padx=10, pady=10))
        self._uiElements.append(MARCUP(element=self.buttonSearch, type=TYPES_UI_MARKUP.GRID, row=0, column=3, padx=10, pady=10))
        if user.role == Roles.getRole(RolesInt.ADMIN):
            self._uiElements.append(MARCUP(element=self.buttonCreate, type=TYPES_UI_MARKUP.GRID, row=0, column=4, padx=10, pady=10))
            self._uiElements.append(MARCUP(element=self.buttonRemove, type=TYPES_UI_MARKUP.GRID, row=0, column=5, pady=10, padx=10))

        self.exitFrame = CTkFrame(master)
        self.buttonBack = CTkButton(self.exitFrame, text=Constants.BUTTON_BACK, font=Constants.FONT, command=commands["back"])
        self._uiElements.append(MARCUP(element=self.exitFrame, type=TYPES_UI_MARKUP.GRID, row=0, column=6, padx=10, pady=10, sticky=E))
        self._uiElements.append(MARCUP(element=self.buttonBack, type=TYPES_UI_MARKUP.PACK, padx=10, pady=10))
        self.show()
