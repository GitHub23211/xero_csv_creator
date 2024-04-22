from tkinter import messagebox
from .add_store import AddStore

class EditStore(AddStore):
    def __init__(self, root):
        AddStore.__init__(self, root)
        self.old_key = ''

    def save_details(self, new_key, new_store):
        try:
            self.master.edit_store(self.old_key, new_key, new_store)
        except Exception as e:
            raise e
        
    def set_entries(self, num, name, price):
        self.old_key = str(num)
        self.store_num_var.set(num)
        self.store_name_var.set(name)
        self.store_price_var.set(price[1:])