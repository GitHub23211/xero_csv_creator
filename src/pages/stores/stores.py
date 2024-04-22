from tkinter.messagebox import askyesno
from components.top import Top
from .add_store import AddStore
from .store_list import StoreList
from .edit_store import EditStore

class Stores(Top):
    def __init__(self, root, model, width, height, close_win_handler):
        Top.__init__(self, root, model, StoreList, width, height, close_win_handler)
        self.pricing = self.model.pricing
        self.columnconfigure(0, weight=1)
        self.curr_view.build()

    def nav_add_store(self):
        self.switch_view(AddStore)
        self.curr_view.build()
    
    def nav_store_list(self):
        self.switch_view(StoreList)
        self.curr_view.build()
    
    def nav_edit_store(self, store_info):
        self.switch_view(EditStore)
        self.curr_view.set_entries(*store_info)
        self.curr_view.build()
    
    def search_stores(self, term):
        return self.pricing.get(term)
    
    def add_new_store(self, key, value):
        if key in self.pricing:
            raise Exception('Store already exists')

        self.pricing.update({key: value})
        self.save_pricing()
        self.nav_store_list()
    
    def edit_store(self, old_key, new_key, value):
        if new_key in self.pricing:
            replace = askyesno('Warning', f'Overwrite the details of store {new_key}?')
            if replace is False:
                return
            
        self.focus()
        del self.pricing[str(old_key)]

        self.pricing.update({new_key: value})
        self.save_pricing()
        self.nav_store_list()
    
    def delete_store(self, key):
        del self.pricing[key]
        self.save_pricing()

    def sort_pricing(self):
        self.pricing = dict(sorted(self.pricing.items(), key=lambda x: self.sort_helper(x[1][0])))

    def save_pricing(self):
        self.sort_pricing()
        self.model.update_pricing(self.pricing)

    def sort_helper(self, element):
        if isinstance(element, str):
            return -1
        return int(element)