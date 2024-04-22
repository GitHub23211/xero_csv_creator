from tkinter import Frame, StringVar, messagebox
from .components.price_treeview import PriceTreeView
from .components.search_bar import SearchBar
from .components.pricing_buttons import PricingButtons

class StoreList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.search_term = StringVar(value='')
        self.price_list = PriceTreeView(self)
        self.search_bar = SearchBar(self)
        self.buttons = PricingButtons(self)
        self.tree = None
    
    def generate_tree(self, items):
        if len(self.tree.get_children()) > 0:
            for i in self.tree.get_children():
                self.tree.delete(i)

        for item in items:
            self.tree.insert('', 'end', text='', iid=item[0], values=(item[0], item[1], f'${item[2]}'))

    def search_stores(self):
        term = self.search_term.get()
        if term == '': return

        stores = self.master.search_stores(term)
        if stores is None:
            messagebox.showerror('Error', 'No store with that store number')
            self.focus()
            return

        results = [stores]
        self.generate_tree(results)
        self.search_term.set('')

    def reset_stores(self):
        self.search_term.set('')
        self.generate_tree(self.master.pricing.values())
    
    def edit_store(self):
        selected_store = self.tree.item(self.tree.focus())['values']
        if len(selected_store) <= 0: return
        self.master.nav_edit_store(selected_store)
    
    def delete_store(self):
        store = self.tree.focus()
        if store != '':
            delete = messagebox.askyesno('Store Delete', f'Are you sure you want to delete store {store}?')
            if delete:
                self.master.delete_store(store)
                self.tree.delete(store)
            self.focus()

    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='EW')

        self.price_list.build()
        self.search_bar.build()
        self.buttons.build()

        self.tree = self.price_list.get_tree()
        self.generate_tree(self.master.pricing.values())