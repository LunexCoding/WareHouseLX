from tkinter import ttk
from tkinter.ttk import Treeview, Scrollbar
from datetime import datetime

import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton

from .context import Context
from .consts import Constants
from settingsConfig import g_settingsConfig


class IncomingDocumentsWindowContext(Context):
    def __init__(self, window, data):
        super().__init__(window, data)
        self.referenceList = []

        self.buttonFrame = CTkFrame(window)
        self.userRoleFrame = CTkFrame(self.buttonFrame)
        self.userRoleLabel = CTkLabel(self.userRoleFrame, text=g_settingsConfig.role, font=("Helvetica", 30))

        self.userRoleLabel.pack(side="left", padx=10, pady=10)
        self.userRoleFrame.pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(self.buttonFrame, text="Склад", font=("Helvetica", 30)).pack(side="left", padx=10, pady=10)
        self.buttonFrame.pack(side="top", fill="x", pady=10, padx=10)

        self.buttonCreateDoc = ctk.CTkButton(self.buttonFrame, text="Создать документ", font=("Helvetica", 30))
        self.buttonCreateDoc.pack(side="left", padx=10, pady=10)
        self.buttonSearch = ctk.CTkButton(self.buttonFrame, text="Найти", font=("Helvetica", 30))
        self.buttonSearch.pack(side="left", padx=10, pady=10)
        self.searchEntry = ctk.CTkEntry(self.buttonFrame, font=("Helvetica", 25), width=200)
        self.searchEntry.pack(side="left", padx=10, pady=10)
        self.buttonClear = ctk.CTkButton(self.buttonFrame, text="Очистить", font=("Helvetica", 30))
        self.buttonClear.pack(side="left", padx=10, pady=10)
        self.buttonRemove = ctk.CTkButton(self.buttonFrame, text="Удалить", font=("Helvetica", 30))
        self.buttonRemove.pack(side="left", padx=10, pady=10)
        self.buttonBack = CTkButton(self.buttonFrame, text="Назад", font=("Helvetica", 30), command=self._onButtonExit)
        self.buttonBack.pack(side="left", padx=10, pady=10)

        self.tableFrame = ctk.CTkFrame(window)
        self.tableFrame.pack(side="top", fill="both", expand=True, pady=10, padx=10)
        self.create_table()

    def _onButtonExit(self):
        window = self._window
        self.clear()
        window.returnToPrevious()

    def create_reference_window(self):
        reference_window = ctk.CTk()
        reference_window.title("Создание справочника")
        next_number = len(self.referenceList) + 1
        label_name = ctk.CTkLabel(reference_window, text="Наименование:")
        label_name.pack()
        entry_name = ctk.CTkEntry(reference_window)
        entry_name.pack()
        label_description = ctk.CTkLabel(reference_window, text="Описание:")
        label_description.pack()
        entry_description = ctk.CTkEntry(reference_window)
        entry_description.pack()
        label_price = ctk.CTkLabel(reference_window, text="Цена:")
        label_price.pack()
        entry_price = ctk.CTkEntry(reference_window)
        entry_price.pack()
        button_save = ctk.CTkButton(reference_window, text="Сохранить", command=lambda: self.save_reference(
            str(next_number), entry_name.get(), entry_description.get(), entry_price.get(),
            "", "", reference_window))
        button_save.pack(side="right", padx=10, pady=10)
        reference_window.mainloop()

    def save_reference(self, number, name, description, price, creation_date, modification_date, reference_window):
        current_date = datetime.now()
        new_data = (number, name, description, price, current_date, modification_date, "")
        self.tree.insert("", "end", values=new_data)
        self.referenceList.append(new_data)
        reference_window.destroy()

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

    def create_table(self):
        self.tree = ttk.Treeview(self.tableFrame, columns=list(Constants.PARISH_DOCUMENT_WINDOW_TREE_OPTIONS.keys()))
        for header, option in Constants.PARISH_DOCUMENT_WINDOW_TREE_OPTIONS.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"])
        self.tree.column("#0", width=0, stretch=False)

        self.tree_scroll = ttk.Scrollbar(self.tableFrame, orient="vertical", command=self.tree.yview)
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
