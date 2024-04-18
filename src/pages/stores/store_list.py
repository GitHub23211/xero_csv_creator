from tkinter import Frame, Label, Button, Entry, Scrollbar, StringVar, messagebox, ttk

DEFAULT_COL_WIDTH = 200 # As per Tkinter Treeview docs

class StoreList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.search_term = StringVar(value='')
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
        self.generate_tree(self.master.prices.values())
    
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

    def store_list(self):
        f = Frame(self)
        f.grid(rowspan=2)
        ID_COL_WIDTH = int(DEFAULT_COL_WIDTH * 0.5)
        NAME_COL_WIDTH = int(DEFAULT_COL_WIDTH * 1)
        PRICE_COL_WIDTH = int(DEFAULT_COL_WIDTH * 0.5)

        self.tree = ttk.Treeview(f)
        self.tree['columns'] = ('id', 'name', 'price')
        self.tree.column('#0', width=0)
        self.tree.column('id', w=ID_COL_WIDTH)
        self.tree.column('name', w=NAME_COL_WIDTH)
        self.tree.column('price', w=PRICE_COL_WIDTH)
        self.tree.heading('id', text='Store No.', anchor='w')
        self.tree.heading('name', text='Store Name', anchor='w')
        self.tree.heading('price', text='Store Pricing', anchor='w')
        
        scroll = Scrollbar(f, orient='vertical', command=self.tree.yview)
        self.tree.config(yscrollcommand=scroll.set)
        self.tree.config(height=20)
        self.tree.bind('<FocusOut>', lambda e: self.tree.selection_remove(self.tree.focus()))

        scroll.grid(row=0, column=1, sticky='NS')
        self.tree.grid(row=0, column=0, sticky='NSEW')

    def search_bar(self):
        f = Frame(self)#, borderwidth=1, background='green')
        f.grid(row=0, column=1, padx=20, sticky='S')

        search_bar_ent = Entry(f, textvariable=self.search_term)
        search_bar_ent.bind('<Return>', lambda e: self.search_stores())

        Label(f, text='Search by Store No.').grid(columnspan=2)
        search_bar_ent.grid(columnspan=2)
        Button(f, text='Search', command=self.search_stores).grid(row=2, column=0, sticky='EW')
        Button(f, text='Reset', command=self.reset_stores).grid(row=2, column=1, sticky='EW')

    def store_pricing_options(self):
        f = Frame(self)#, borderwidth=1, background='red')
        f.grid(row=1, column=1, sticky='N', pady=20)
        Button(f, text='Add Store Pricing', command=self.master.nav_add_store).grid(row=1, column=0, sticky='EW')
        Button(f, text='Edit Store Pricing', command=self.edit_store).grid(row=2, column=0, sticky='EW')
        Button(f, text='Delete Store Pricing', command=self.delete_store).grid(row=3, column=0, sticky='EW')
        
    def build(self):
        self.columnconfigure(0, weight=1)
        self.grid(sticky='EW')
        self.store_list()
        self.search_bar()
        self.store_pricing_options()
        self.generate_tree(self.master.prices.values())