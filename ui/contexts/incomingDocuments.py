from datetime import datetime
from tkinter.ttk import Treeview, Scrollbar

import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton

from .context import Context
from .popup.inputIncomingDocumentsWindow import InputIncomingDocumentsWindowContext
from .consts import Constants
from settingsConfig import g_settingsConfig
from dataStructures.referenceBook import g_incomingDocumentsBook


class IncomingDocumentsWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.referenceList = []

        self.buttonFrame = CTkFrame(window)
        self.userRoleFrame = CTkFrame(self.buttonFrame)
        self.userRoleLabel = CTkLabel(self.userRoleFrame, text=g_settingsConfig.role, font=Constants.FONT)

        self.userRoleLabel.pack(side="left", padx=10, pady=10)
        self.userRoleFrame.pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(self.buttonFrame, text="Склад", font=Constants.FONT).pack(side="left", padx=10, pady=10)
        self.buttonFrame.pack(side="top", fill="x", pady=10, padx=10)

        self.buttonCreateDocument = ctk.CTkButton(self.buttonFrame, text="Создать документ", font=Constants.FONT, command=self._onCreateDocument)
        self.buttonCreateDocument.pack(side="left", padx=10, pady=10)
        self.buttonSearch = ctk.CTkButton(self.buttonFrame, text="Найти", font=Constants.FONT)
        self.buttonSearch.pack(side="left", padx=10, pady=10)
        self.searchEntry = ctk.CTkEntry(self.buttonFrame, font=Constants.FONT, width=200)
        self.searchEntry.pack(side="left", padx=10, pady=10)
        self.buttonClear = ctk.CTkButton(self.buttonFrame, text="Очистить", font=Constants.FONT)
        self.buttonClear.pack(side="left", padx=10, pady=10)
        self.buttonRemove = ctk.CTkButton(self.buttonFrame, text="Удалить", font=Constants.FONT)
        self.buttonRemove.pack(side="left", padx=10, pady=10)
        self.buttonBack = CTkButton(self.buttonFrame, text="Назад", font=Constants.FONT, command=self._onButtonBack)
        self.buttonBack.pack(side="left", padx=10, pady=10)

        self.tableFrame = ctk.CTkFrame(window)
        self.tableFrame.pack(side="top", fill="both", expand=True, pady=10, padx=10)
        self.create_table()
        self._loadRows()

    def _onButtonBack(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def _onCreateDocument(self):
        self._window.openTopLevel(
            InputIncomingDocumentsWindowContext,
            {
                "name": "Создание документа прихода",
                "command": self._saveDocument
            }
        )

    def _saveDocument(self, data):
        print(data)
        self._window.topLevelWindow.close()
        self.tree.insert("", "end", values=list(data.values()))
        # self.referenceList.append(data)

    def search_records(self):
        search_term = self.entry_field.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)
        if not search_term:
            for record in self.referenceList:
                self.tree.insert("", "end", values=record)
        else:
            for record in self.referenceList:
                if search_term in record[1].lower():
                    self.tree.insert("", "end", values=record)

    def _loadRows(self):
        g_incomingDocumentsBook.loadRows()
        for row in g_incomingDocumentsBook.rows:
            self.referenceList.append(row)
            self.tree.insert("", "end", values=list(row.values()))

    def create_table(self):
        self.tree = Treeview(self.tableFrame, columns=list(Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS.keys()))
        for header, option in Constants.INCOMING_AND_OUTGOING_WINDOWS_TREE_OPTIONS.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"], anchor="center")
        self.tree.column("#0", width=0, stretch=False)

        self.tree_scroll = Scrollbar(self.tableFrame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<Double-1>", self.edit_record)

    def edit_record(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            edit_window = ctk.CTk()
            edit_window.title("Изменение справочника")
            label_name = ctk.CTkLabel(edit_window, text="Наименование:")
            label_name.pack()
            entry_name = ctk.CTkEntry(edit_window)
            entry_name.pack()
            entry_name.insert(0, values[1])
            label_description = ctk.CTkLabel(edit_window, text="Описание:")
            label_description.pack()
            entry_description = ctk.CTkEntry(edit_window)
            entry_description.pack()
            entry_description.insert(0, values[2])
            label_price = ctk.CTkLabel(edit_window, text="Цена:")
            label_price.pack()
            entry_price = ctk.CTkEntry(edit_window)
            entry_price.pack()
            entry_price.insert(0, values[3])
            button_save = ctk.CTkButton(edit_window, text="Сохранить", command=lambda: self.save_edit(selected_item, values[0], entry_name.get(), entry_description.get(), entry_price.get(), "", edit_window))
            button_save.pack(side="right", padx=10, pady=10)
            edit_window.mainloop()

    def save_edit(self, selected_item, number, name, description, price, _, edit_window):
        creation_date = self.tree.item(selected_item, "values")[4]
        modification_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tree.item(selected_item, values=(number, name, description, price, creation_date, modification_date, ""))
        index = self.tree.index(selected_item)
        self.reference_list[index] = (
            number, name, description, price, creation_date, modification_date, "")
        edit_window.destroy()

    def clear_entry(self):
        self.entry_field.delete(0, "end")
        for item in self.tree.get_children():
            self.tree.delete(item)
        for record in self.reference_list:
            self.tree.insert("", "end", values=record)
