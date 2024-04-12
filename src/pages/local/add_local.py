from tkinter import Frame, messagebox

from .components.man_info_input import ManInfoInput
from .components.store_nums_input import StoreNumsInput
from .components.man_list import ManList

class AddLocal(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.num_added = []
        self.man_info_input = ManInfoInput(self)
        self.man_list = ManList(self)
        self.store_nums_input = StoreNumsInput(self, self.get_button_commands())
        self.master.bind('<Return>', self.add_manifest)
        self.set_date()
    
    def add_manifest(self, event=None):
        man_num = self.man_info_input.get_man_num()
        man_date = self.man_info_input.get_man_date()
        store_nums = self.store_nums_input.get_store_nums()
        loaded = self.store_nums_input.get_loaded()
        
        try:
            self.num_added.append(self.master.add_manifest(man_num, man_date, store_nums, loaded))
            self.update_list_view()
            self.reset_widgets()
        except Exception as e:
            self.show_error(e)
    
    def delete_manifest(self):
        try:
            last_num_added = self.num_added.pop()
            self.master.delete_manifest(last_num_added)
            
            num_manifests = self.master.get_num_manifests()
            self.man_list.delete_last_item(num_manifests, last_num_added)
        except Exception as e:
            self.show_error(e)

    def save_csv(self):
        try:
            self.master.save_csv()
        except Exception as e:
            self.show_error(e)
    
    def get_button_commands(self):
        add = self.add_manifest
        delete = self.delete_manifest
        save = self.save_csv

        return {
            'add': add,
            'delete': delete,
            'save': save
        }
    
    def set_date(self):
        date = self.master.get_inv_date()
        self.man_info_input.set_man_date(date)   
    
    def reset_widgets(self):
        self.store_nums_input.reset_loaded()
        self.store_nums_input.reset_store_nums()
        self.man_info_input.reset_man_num()
        self.man_info_input.return_focus()
        self.man_list.reset_view()

    def update_list_view(self):
        last_num_added = self.num_added[len(self.num_added) - 1]
        latest_entries = self.master.get_invoice()[-last_num_added:]
        num_manifests = self.master.get_num_manifests()
        
        self.man_list.update_view(latest_entries, num_manifests)

    def build(self):
        self.grid()
        self.man_info_input.build()
        self.store_nums_input.build()
        self.man_list.build()
    
    def show_error(self, e):
        messagebox.showerror('Error', e)
        self.man_info_input.return_focus()