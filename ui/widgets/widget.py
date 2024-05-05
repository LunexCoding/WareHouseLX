from customtkinter import CTkBaseClass

from .markup import TYPES_UI_MARKUP


class BaseWidget(CTkBaseClass):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self._uiElements = []
        self._visibility = True

    def hide(self):
        self._visibility = False
        for markup in self._uiElements:
            if markup.type == TYPES_UI_MARKUP.PACK:
                markup.element.pack_forget()
            elif markup.type == TYPES_UI_MARKUP.GRID:
                markup.element.grid_forget()

    def show(self):
        self._visibility = True
        for markup in self._uiElements:
            if markup.type == TYPES_UI_MARKUP.PACK:
                padx, pady = markup.padx, markup.pady
                side, fill = markup.side, markup.fill
                expand = markup.expand
                markup.element.pack(padx=padx, pady=pady, side=side, fill=fill, expand=expand)
            elif markup.type == TYPES_UI_MARKUP.GRID:
                padx, pady, sticky = markup.padx, markup.pady, markup.sticky
                row, column = markup.row, markup.column
                markup.element.grid(padx=padx, pady=pady, sticky=sticky, row=row, column=column)

    @property
    def visibility(self):
        return self._visibility
