import customtkinter as ctk
from customtkinter import CTkButton

from .context import Context
from .referenceWindow import ReferenceWindow
from .inputWindow import InputWindowContext


class DirectoryReportWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.referenceList = []
        self.buttonSaveCreated = False

        self.frame = ctk.CTkFrame(window)
        self.frame.pack(side="top",  pady=10, padx=10)
        self.buttonBack = ctk.CTkButton(self.frame, text="назад", font=("Helvetica", 30), command=self._onButton1)
        self.buttonBack.pack(side="right", padx=10, pady=10)
        self.buttonCreateDoc = ctk.CTkButton(self.frame, text="Создать справочник", font=("Helvetica", 30), command=self.createReferenceWindow)
        self.buttonCreateDoc.pack(side="right", padx=10, pady=10)
        self.frameItems = ctk.CTkFrame(window)
        self.frameItems.pack(side="top", fill="both", expand=True, pady=0, padx=10)

    def _onButton1(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def createReferenceWindow(self):
        if not self.buttonSaveCreated:
            self._window.openTopLevel(InputWindowContext, {"name": "Input Window"})
            buttonSave = CTkButton(self._window.topLevelWindow, text="Сохранить", command=lambda: self.saveReference(self._window.topLevelWindow.context.priceEntry.get()))
            buttonSave.pack(side="right", padx=10, pady=10)
            self.buttonSaveCreated = True

    def saveReference(self, name):
        reference = {"Наименование": name}
        self.referenceList.insert(0, reference)
        self.updateReferenceFrame()
        self._window.topLevelWindow.close()
        self.buttonSaveCreated = False

    def showReference(self, reference):
        selectedName = reference['Наименование']
        self.createReferenceInfoWindow(selectedName)

    def createReferenceInfoWindow(self, referenceName):
        self._window.openTopLevel(ReferenceWindow, data={"name": referenceName})

    def updateReferenceFrame(self):
        for widget in self.frameItems.winfo_children():
            widget.destroy()
        row, col = 0, 0
        for reference in self.referenceList:
            button = ctk.CTkButton(self.frameItems, text=reference['Наименование'], command=lambda ref=reference: self.showReference(reference))
            button.pack(padx=20, pady=20)
            row += 1
            if row * 50 > self.frameItems.winfo_height():
                row = 0
                col += 1
        self.frameItems.update_idletasks()
