from customtkinter import CTkButton, CTkFrame, Y

from ui.widgets import PageNameWidget, UserInfoWidget
from user import g_user

from .consts import Constants
from .context import Context
from .ordersContext import OrdersContext


class MainWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)

        self.frame = CTkFrame(window)

        UserInfoWidget(self.frame, g_user)
        PageNameWidget(self.frame, Constants.PAGE_MAIN)

        self.buttonFrame = CTkFrame(self.frame)
        self.buttonOpenOrdersContext = CTkButton(self.buttonFrame, text=Constants.PAGE_ORDERS, font=Constants.FONT, command=self._onButtonOpenOrdersContextClicked)

        self.buttonOpenOrdersContext.grid(row=0, column=2, padx=10, pady=10)
        self.buttonFrame.grid(row=0, column=1, padx=10, pady=10)

        self.exitFrame = CTkFrame(self.frame)
        self.buttonExit = CTkButton(self.exitFrame, text=Constants.BUTTON_EXIT, font=Constants.FONT, command=self._onButtonExit)
        self.buttonExit.pack(padx=10, pady=10)
        self.exitFrame.grid(row=0, column=2, padx=10, pady=10)

        self.frame.pack(fill=Y, padx=10, pady=10)

    def _onButtonOpenOrdersContextClicked(self):
        window = self._window
        self.clear()
        window.changeContext(OrdersContext)

    def _onButtonExit(self):
        self._window.close()
