from tkinter import messagebox
from .add_store import AddStore

class EditStore(AddStore):
    def __init__(self, root):
        AddStore.__init__(self, root)
        self.original_key = ''

    def set_entries(self, num, name, price):
        self.original_key = num
        self.store_num_var.set(num)
        self.store_name_var.set(name)
        self.store_price_var.set(price[1:])
    
    def save_details(self):
        try:
            new_key = self.store_num_var.get()
            store = [
                    int(new_key),
                    self.store_name_var.get(),
                    self.store_price_var.get()
                ]
            self.master.edit_store(self.original_key, new_key, store)
        except Exception as e:
            messagebox.showerror('Error', e)
            self.focus()